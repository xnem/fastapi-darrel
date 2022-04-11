from sqlalchemy import Column, String, Integer, Numeric
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.sql.expression import text

from database import Base as base_calc_history_details


class CalculationHistoryDetails(base_calc_history_details):
    __tablename__ = 'calculation_history_details'

    id = Column(String(50), primary_key=True)
    calculation_history_id = Column(Integer)
    driver_name = Column(String(50))
    driver_surname = Column(String(50))
    calculated_price = Column(Numeric(7, 2))
    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    updated_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), onupdate=text('CURRENT_TIMESTAMP'))
