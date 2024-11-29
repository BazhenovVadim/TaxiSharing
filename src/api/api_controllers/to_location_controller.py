from fastapi import APIRouter
from src.services import To_location_service
router = APIRouter(prefix="/to_location", tags=["to_location"])
@router.get("/to_location/")
async def get_to_location(to_location: str):
    place_to = await To_location_service.process_to_location(to_location)
    return place_to