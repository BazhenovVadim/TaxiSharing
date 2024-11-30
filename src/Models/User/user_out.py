from .user_in import UserIn


class UserOut(UserIn):
    user_id: int

    class Config:
        orm_mode: True
