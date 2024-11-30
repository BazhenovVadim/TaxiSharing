from .user_in import UserIn


class UserOut(UserIn):
    user_id: int

    class Config:
        from_attributes: True
