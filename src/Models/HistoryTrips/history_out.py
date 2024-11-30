from src.Models.HistoryTrips import HistoryIn

class HistoryOut(HistoryIn):
    id_history_trip : int

    class Config:
        from_attributes : True