import version
import api_data
from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()

# simple version endpoint, uses function print_version to display current app version
@router.get("/version")
async def appversion():
    return {"version": version.get_version()}

@router.get("/temperature")
async def temperature():
    return {"average temperature": api_data.average_temps}

app.include_router(router)