from typing import List
import logging

from sqlalchemy import desc
from sqlalchemy.orm import Session
import models.calculation_history_details as calc_history_details_model
import models.calculation_histories as calc_history_model
import sys
import models.history as history_model


logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


def get_histories(db: Session) -> List[history_model.History]:
    histories = db.query(
        calc_history_model.CalculationHistories,
        calc_history_details_model.CalculationHistoryDetails
    ).join(calc_history_model.CalculationHistories,
           calc_history_model.CalculationHistories.cheapest_history_detail_id ==
           calc_history_details_model.CalculationHistoryDetails.id
           ).order_by(desc(calc_history_model.CalculationHistories.updated_at)).all()

    return histories
