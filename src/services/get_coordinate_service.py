import requests


def address_to_coords_osm(address: str):
    """
    Преобразует адрес в координаты с использованием Nominatim API (OpenStreetMap).
    :param address: Строка с адресом (например, "ул. Карбышева, 10, Санкт-Петербург").
    :return: Кортеж с координатами (широта, долгота) или None, если адрес не найден.
    """
    try:
        url = "https://nominatim.openstreetmap.org/search"
        params = {"q": address, "format": "json", "addressdetails": 1}
        response = requests.get(url, params=params, headers={"User-Agent": "FastAPIApp"})

        if response.ok:
            data = response.json()
            if data:
                lat = float(data[0]["lat"])
                lon = float(data[0]["lon"])
                return lat, lon
        return None
    except Exception as e:
        print(f"Ошибка при получении координат: {e}")
        return None