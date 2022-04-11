from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import cruds.history as history_crud

router = APIRouter()


@router.get("/v1/histories")
def get_histories(db: Session = Depends(get_db)):
    return history_crud.get_histories(db)


@router.get("/histories/{history_id}/details")
def get_history_details():
    pass


@router.post("/histories")
def post_history():
    pass


@router.post("/histories/{history_id}")
def post_history_details():
    pass


@router.post("/drivers")
def post_driver():
    pass
