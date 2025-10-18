import version
import api_data
from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()

@router.get("/version")
async def appversion():
    return {"version": version.get_version()}

@router.get("/temperature")
async def temperature():
    if api_data.average_temps <= 10:
        return {"average temperature": f"{api_data.average_temps} (Too Cold)"}
    elif 10 < api_data.average_temps <=36:
        return {"average temperature": f"{api_data.average_temps} (Good)"}
    elif api_data.average_temps > 36:
        return {"average temperature": f"{api_data.average_temps} (Too Hot)"}
    else:
        return {"warning": "error in temperature calculation"}
    
app.include_router(router)