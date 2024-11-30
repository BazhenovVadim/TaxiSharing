from fastapi import APIRouter
from src.services import To_location_service
from src.services.data_storage import set_location

router = APIRouter(prefix="/to_location", tags=["to_location"])


@router.post("/to_location/")
async def get_to_location(to_location: str):
    set_location("to_location", to_location)
    return {"message": "To location saved", "to_location": to_location}

