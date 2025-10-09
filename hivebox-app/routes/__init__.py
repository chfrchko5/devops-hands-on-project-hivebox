import version
from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()

# simple version endpoint, uses function print_version to display current app version
@router.get("/version")
async def appversion():
    return {"version": version.print_version()}

@router.get("/temperature")
async def temperature():
    


app.include_router(router)