from .base_meta import BaseSQLAlchemyModel
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class User(BaseSQLAlchemyModel):
    __tablename__ = "User"

    user_id = Column(Integer,autoincrement=True, primary_key=True)
    user_name = Column(String, nullable=False)
    login = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    #day_result = relationship("DayResults", back_populates="user")

    def __str__(self):
        return f"{self.user_id} {self.user_name} {self.login}"

    def __repr__(self):
        return str(self)
