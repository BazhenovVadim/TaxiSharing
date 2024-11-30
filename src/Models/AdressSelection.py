from pydantic import BaseModel


class AdressSelection(BaseModel):
    from_address: str
    to_address: str