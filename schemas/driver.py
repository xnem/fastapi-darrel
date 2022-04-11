from datetime import datetime
from pydantic import BaseModel


class DriverBase(BaseModel):
    name: str
    surname: str
    email: str
    base_taxi_price: float
    base_taxi_distance: float


class Driver(DriverBase):
    id: int
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class DriverCreate(DriverBase):
    pass


class DriverCreateResponse(DriverBase):
    id: int

    class Config:
        orm_mode = True

