from fastapi import APIRouter, HTTPException

from src.Models import AdressSelection
from src.services.data_storage import available_addresses, pier_data

router = APIRouter(prefix="/addresses")


@router.get("/addresses/")
async def get_addresses():
    return {"available_addresses": available_addresses}


@router.post("/validate_addresses/")
async def validate_addresses(selection: AdressSelection):
    if selection.from_address not in available_addresses:
        raise HTTPException(status_code=400, detail="Адрес отправления отсутствует в списке доступных")
    if selection.to_address not in available_addresses:
        raise HTTPException(status_code=400, detail="Адрес назначения отсутствует в списке доступных")

    # Получение координат
    from_coords = next(
        (pier for pier in pier_data.values() if f"{pier['Название причала']} — {pier['Адрес причала']}" == selection.from_address),
        None
    )
    to_coords = next(
        (pier for pier in pier_data.values() if f"{pier['Название причала']} — {pier['Адрес причала']}" == selection.to_address),
        None
    )

    return {
        "message": "Адреса успешно проверены",
        "from_address": selection.from_address,
        "to_address": selection.to_address,
        "from_coordinates": {
            "latitude": from_coords["Широта причала"],
            "longitude": from_coords["Долгота причала"]
        },
        "to_coordinates": {
            "latitude": to_coords["Широта причала"],
            "longitude": to_coords["Долгота причала"]
        }
    }
