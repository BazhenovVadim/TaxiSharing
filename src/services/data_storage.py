data_storage = {
    "from_location": None,
    "to_location": None,
}

def set_location(key: str, value: str):
    data_storage[key] = value

def get_location(key: str):
    return data_storage.get(key)