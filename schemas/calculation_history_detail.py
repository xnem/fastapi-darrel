from datetime import datetime
from pydantic import BaseModel


class CalculationHistoryDetail(BaseModel):
    id: str
    calculation_history_id: int
    driver_name: str
    driver_surname: str
    calculated_price: float
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
