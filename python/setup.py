import sqlite3
import os
from etl_pipeline import run_etl


DATABASE = "../database/game_market_analysis.db"
CREATE_TABLES = "../sql/create_tables.sql"


def create_database():

    if os.path.exists(DATABASE):
        os.remove(DATABASE)

    conn = sqlite3.connect(DATABASE)

    with open(CREATE_TABLES, "r") as file:
        sql_script = file.read()

    conn.executescript(sql_script)

    conn.close()

    print("Database created successfully")


if __name__ == "__main__":

    create_database()

    run_etl()

    print("ETL completed")