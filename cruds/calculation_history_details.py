import logging
import sys
from typing import List

from sqlalchemy import desc
from sqlalchemy.orm import Session
import models.calculation_history_details as calc_history_details_model


logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


def get_calc_history_details(calc_history_id: int, db: Session) -> List[calc_history_details_model.CalculationHistoryDetails]:
    return db.query(calc_history_details_model.CalculationHistoryDetails).\
        filter(calc_history_details_model.CalculationHistoryDetails.calculation_history_id == calc_history_id).\
        order_by(calc_history_details_model.CalculationHistoryDetails.calculated_price).\
        all()
