from pydantic import BaseModel


class LocationRequest(BaseModel):
    from_address: str
    to_address: str