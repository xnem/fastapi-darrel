from pydantic import BaseModel
from datetime import datetime


class History(BaseModel):
    cheapest_history_detail_id: str
    updated_at: datetime
    input_distance: float
    calculated_price: float
    driver_name: str
    driver_surname: str
