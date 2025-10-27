import version
import api_data
from fastapi import FastAPI, APIRouter, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator
import redis
import os

valkey_host = os.getenv("VALKEY_HOST", "localhost")
valkey_port = int(os.getenv("VALKEY_PORT", 6379))

valkey = redis.Redis(
    host=valkey_host,
    port=valkey_port,
    db=0,
    decode_responses=True
)

app = FastAPI()
router = APIRouter()

Instrumentator().instrument(app).expose(app)

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
        return {"average temperature": cached_value, "cached": True}
    
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

app.include_router(router)