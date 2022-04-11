from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.sql.expression import text

from database import Base as base_calc_histories


class CalculationHistories(base_calc_histories):
    __tablename__ = 'calculation_histories'

    id = Column(Integer, primary_key=True, autoincrement=False)
    cheapest_history_detail_id = Column(String(50))
    input_distance = Column(Numeric(7, 2))
    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    updated_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), onupdate=text('CURRENT_TIMESTAMP'))
