import version
import api_data
from fastapi import FastAPI, APIRouter, HTTPException, Response, status
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter
import redis
import os


valkey = None
if not os.getenv("SKIP_VALKEY"):
    valkey = redis.Redis(
        host=os.getenv("VALKEY_HOST", "localhost"),
        port=int(os.getenv("VALKEY_PORT", 6379)),
        db=0,
        decode_responses=True
    )
    
app = FastAPI()
router = APIRouter()

Instrumentator().instrument(app).expose(app)

cache_hits = Counter("cache_hits_total", "Number of successful cache hits")
cache_misses = Counter("cache_misses_total", "Number of cache misses")

CACHE_KEY_TEMPERATURE = "average_temperature"
CACHE_TTL_SECONDS = 60

def get_temp(temp: float) -> str:
    if temp <= 10:
        return f"{round(temp, 2)} (Too Cold)"
    elif 10 < temp <= 36:
        return f"{round(temp, 2)} (Good)"
    elif temp > 36:
        return f"{round(temp, 2)} (Too Hot)"
    else:
        raise ValueError("error in temperature calculation")
    
@router.get("/version")
async def appversion():
    return {"version": version.__version__}

@router.get("/temperature")
async def temperature():
    cached_value = valkey.get(CACHE_KEY_TEMPERATURE)
    if cached_value is not None:
        cache_hits.inc()
        return {"average temperature": cached_value, "cached": True}
    
    cache_misses.inc()
    
    try:
        avg = float(api_data.average_temps)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    try:
        classified = get_temp(avg)
    except ValueError as e:
        return {"warning": str(e)}
    
    valkey.setex(CACHE_KEY_TEMPERATURE, CACHE_TTL_SECONDS, classified)
    return {"average temperature": classified, "cached": False}

@router.get("/readyz")
async def api_ready():
    if api_data.health_check(api_data.urls):
        return Response(status_code=status.HTTP_200_OK)
    else:
        return Response(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

app.include_router(router)