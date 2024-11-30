from fastapi import APIRouter
from src.services import From_location_service
from src.services.data_storage import set_location

router = APIRouter(prefix="/from_location", tags=["from_location"])


@router.post("/from_location/")
async def get_from_location(from_location: str):
    set_location("from_location", from_location)
    return {"message": "From location saved", "from_location": from_location}

