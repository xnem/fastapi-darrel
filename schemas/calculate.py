from pydantic import BaseModel


class CalculateRequest(BaseModel):
    moving_distance: float
    additional_distance_unit: float
    distance_unit_price: float
