from pydantic import BaseModel


class UserIn(BaseModel):
    user_name: str
    login: str
    email: str
    password: str

    class Config:
        orm_mode: True
