import logging
import sys
from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
import schemas.driver as driver_schema
import cruds.driver as driver_crud
from database import get_db

router = APIRouter()
logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


@router.get("/v1/drivers", response_model=List[driver_schema.Driver])
def get_drivers(db: Session = Depends(get_db)):
    return driver_crud.get_drivers(db)


@router.get("/v1/drivers/{driver_id}", response_model=driver_schema.Driver)
def get_driver(driver_id: int, db: Session = Depends(get_db)):
    logger.info(driver_id)
    return driver_crud.get_driver(driver_id, db)


@router.put("/v1/drivers/{driver_id}", response_model=driver_schema.DriverCreate)
def put_driver(driver_id: int, driver_body: driver_schema.DriverCreate):
    return driver_schema.DriverCreateResponse(id=driver_id, **driver_body.dict())


@router.delete("/v1/drivers/{driver_id}", response_model=None)
def delete_driver(driver_id: int):
    return


@router.post("/v1/drivers", response_model=driver_schema.DriverCreateResponse)
def post_driver(driver_body: driver_schema.DriverCreate, db: Session = Depends(get_db)):
    return driver_crud.create_driver(db, driver_body)
