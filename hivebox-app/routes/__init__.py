import version
import api_data
from fastapi import FastAPI, APIRouter
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
router = APIRouter()

Instrumentator().instrument(app).expose(app)
 
@router.get("/version")
async def appversion():
    return {"version": version.get_version()}

@router.get("/temperature")
async def temperature():
    if api_data.average_temps <= 10:
        return {"average temperature": f"{round(api_data.average_temps, 2)} (Too Cold)"}
    elif 10 < api_data.average_temps <=36:
        return {"average temperature": f"{round(api_data.average_temps, 2)} (Good)"}
    elif api_data.average_temps > 36:
        return {"average temperature": f"{round(api_data.average_temps, 2)} (Too Hot)"}
    else:
        return {"warning": "error in temperature calculation"}
    
app.include_router(router)