import logging
import sys
import uuid

from sqlalchemy import func
from sqlalchemy.orm import Session
import schemas.calculate as calculate_schema
from cruds.driver import get_drivers
import models.calculation_histories as calc_histories_model
from models.calculation_history_details import CalculationHistoryDetails

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


def calculate(calculate_request: calculate_schema.CalculateRequest, db: Session) -> int:
    cheapest_fare = 0
    cheapest_history_detail_id = ""
    index = 0
    drivers = get_drivers(db)

    # calculation_historiesの最大id取得してプラス1する
    max_id = db.query(func.max(calc_histories_model.CalculationHistories.id).label("id")).one()
    logger.info(f"最大idは{max_id.id}")
    max_id = int(max_id.id) + 1

    # calculation_history_detailsデータを作成していく
    #   id = UUID (DB側で連番にするとcalculation_historiesデータ作成時にきついか)
    #   calculation_history_id = 上記でプラス1した数値
    #   driver_name = driver.name
    #   calculated_price = 下記計算の結果
    for driver in drivers:
        distance_subject_to_additional_fare = calculate_request.moving_distance - float(driver.base_taxi_distance)
        if distance_subject_to_additional_fare > 0:
            distance_unit = distance_subject_to_additional_fare / calculate_request.additional_distance_unit
            fare = float(driver.base_taxi_price) + (distance_unit * calculate_request.distance_unit_price)
        else:
            fare = float(driver.base_taxi_price)
        logger.info(f"------{driver.name}------")
        logger.info(fare)

        detail_id = str(uuid.uuid4())
        calc_history_detail = CalculationHistoryDetails()
        calc_history_detail.id = detail_id
        calc_history_detail.calculation_history_id = max_id
        calc_history_detail.driver_name = driver.name
        calc_history_detail.driver_surname = driver.surname
        calc_history_detail.calculated_price = fare
        db.add(calc_history_detail)

        if index == 0 or fare < cheapest_fare:
            cheapest_fare = fare
            cheapest_history_detail_id = detail_id

        index += 1

    # calculation_historiesデータを作成する
    #   id = calculation_history_details.calculation_history_idに共通してインサートした数値
    #   cheapest_history_detail_id = 最安値のid
    #   input_distance = calculate_request.moving_distance
    calc_history = calc_histories_model.CalculationHistories()
    calc_history.id = max_id
    calc_history.cheapest_history_detail_id = cheapest_history_detail_id
    calc_history.input_distance = calculate_request.moving_distance
    db.add(calc_history)

    db.commit()

    return max_id

