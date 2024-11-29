from fastapi import APIRouter
from src.services import From_location_service


router = APIRouter(prefix="/from_location", tags=["from_location"])


@router.get("/from_location/")
async def get_from_location(from_location: str):
    processed_from = await From_location_service.process_from_location(from_location)
    return {"from": processed_from}
