from sqlalchemy import create_engine

from models.driver import base_driver
from models.calculation_histories import base_calc_histories
from models.calculation_history_details import base_calc_history_details

DB_URL = "postgresql://postgres:postgres@127.0.0.1:5432/darrel"
engine = create_engine(DB_URL, echo=True)


def reset_database():
    base_driver.metadata.drop_all(bind=engine)
    base_driver.metadata.create_all(bind=engine)
    base_calc_histories.metadata.drop_all(bind=engine)
    base_calc_histories.metadata.create_all(bind=engine)
    base_calc_history_details.metadata.drop_all(bind=engine)
    base_calc_history_details.metadata.create_all(bind=engine)


# 使い方
#   コンソールでdarrel_pythonにいる状態でpython migrate_db.py
if __name__ == "__main__":
    reset_database()
