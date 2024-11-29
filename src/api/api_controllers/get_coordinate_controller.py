from fastapi import APIRouter
from starlette.exceptions import HTTPException
from src.Models import LocationRequest
from src.api.api_controllers.from_location_controller import get_from_location
from src.api.api_controllers.to_location_controller import get_to_location
from src.services import address_to_coords_osm

router = APIRouter(prefix="/get_coordinates", tags=["get_coordinates"])
@router.post("/get_coordinate/")
async def convert_addresses():

    from_location = await get_from_location()
    to_location = await get_to_location()

    origin_coords = address_to_coords_osm(from_location)
    destination_coords = address_to_coords_osm(to_location)

    if not origin_coords or not destination_coords:
        raise HTTPException(status_code=400, detail="Не удалось найти координаты для одного или обоих адресов")

    return {
        "from_address": from_location,
        "to_address": to_location,
        "from_coordinates": origin_coords,
        "to_coordinates": destination_coords
    }