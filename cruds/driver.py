from typing import List

from sqlalchemy.orm import Session

import schemas.driver as driver_schema
import models.driver as driver_model


def create_driver(db: Session, driver_create: driver_schema.DriverCreate) -> driver_model.Driver:
    driver = driver_model.Driver(**driver_create.dict())
    db.add(driver)
    db.commit()
    db.refresh(driver)
    return driver


def get_drivers(db: Session) -> List[driver_model.Driver]:
    return db.query(driver_model.Driver).all()


def get_driver(driver_id: int, db: Session) -> driver_model.Driver:
    return db.query(driver_model.Driver).get(driver_id)
