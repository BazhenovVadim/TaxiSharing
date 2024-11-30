from pydantic import BaseModel

class HistoryIn(BaseModel):
    trip_start: str
    trip_finish: str
    time_trip: int
    cost_trip: float

    class Config:
        orm_mode = True