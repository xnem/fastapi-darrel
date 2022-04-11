from sqlalchemy import Column, Integer, String, Numeric, Boolean
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.sql.expression import text

from database import Base as base_driver


class Driver(base_driver):
    __tablename__ = 'drivers'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(50))
    surname = Column(String(50))
    email = Column(String(50))
    base_taxi_price = Column(Numeric(7, 2))
    base_taxi_distance = Column(Numeric(7, 2))
    is_deleted = Column(Boolean, server_default=text('False'))
    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    updated_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), onupdate=text('CURRENT_TIMESTAMP'))
