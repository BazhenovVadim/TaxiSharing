from data_base import BaseSQLAlchemyModel


class User(BaseSQLAlchemyModel):
    __tablename__ = "user"

    user_id = Column(Integer,autoincrement=True, primary_key=True)
    user_name = Column(String, nullable=False)
    login = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    day_result = relationship("DayResults", back_populates="user")

    def __str__(self):
        return f"{self.user_id} {self.user_name} {self.login}"

    def __repr__(self):
        return str(self)