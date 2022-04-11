from sqlalchemy import orm
from . import calculation_histories as calc_histories
from . import calculation_history_details as calc_history_details

from database import Base as base_history


class History(base_history):
    __table__ = orm.join(calc_histories.CalculationHistories,
                         calc_history_details.CalculationHistoryDetails,
                         calc_histories.CalculationHistories.cheapest_history_detail_id ==
                         calc_history_details.CalculationHistoryDetails.id)
    cheapest_history_detail_id = orm.column_property(
        calc_histories.CalculationHistories.cheapest_history_detail_id,
        calc_history_details.CalculationHistoryDetails.id
    )
    created_at = orm.column_property(
        calc_histories.CalculationHistories.created_at,
        calc_history_details.CalculationHistoryDetails.created_at
    )
    updated_at = orm.column_property(
        calc_histories.CalculationHistories.updated_at,
        calc_history_details.CalculationHistoryDetails.updated_at
    )
