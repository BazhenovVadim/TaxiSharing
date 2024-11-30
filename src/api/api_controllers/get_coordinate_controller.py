from fastapi import APIRouter, HTTPException
from src.services.data_storage import get_location
from src.services import address_to_coords_osm

router = APIRouter(prefix="/get_coordinates", tags=["get_coordinates"])

@router.post("/convert/")
async def convert_to_coordinates():
    # Берем данные из хранилища
    from_location = get_location("from_location")
    to_location = get_location("to_location")

    # Проверяем, что данные существуют
    if not from_location or not to_location:
        raise HTTPException(status_code=400, detail="Адреса отправления и прибытия не установлены")

    # Преобразуем адреса в координаты
    from_coords = address_to_coords_osm(from_location)
    to_coords = address_to_coords_osm(to_location)

    # Проверяем, что координаты найдены
    if not from_coords or not to_coords:
        raise HTTPException(status_code=400, detail="Не удалось найти координаты для одного или обоих адресов")

    return {
        "from_address": from_location,
        "from_coordinates": from_coords,
        "to_address": to_location,
        "to_coordinates": to_coords
    }
