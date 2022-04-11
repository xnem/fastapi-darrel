import logging
import sys
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.calculate import CalculateRequest
import cruds.domains.calculate as calculate_crud
import cruds.calculation_history_details as calc_history_details_crud
import schemas.calculation_history_detail as calc_history_detail_schema

router = APIRouter()
logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


@router.post("/v1/calculate", response_model=List[calc_history_detail_schema.CalculationHistoryDetail])
def calculate(calculate_model: CalculateRequest, db: Session = Depends(get_db)):
    logger.info(calculate_model)
    calculate_history_id = calculate_crud.calculate(calculate_model, db)
    return calc_history_details_crud.get_calc_history_details(calculate_history_id, db)
