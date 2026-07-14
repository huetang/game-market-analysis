#connecting to database
import sqlite3
import os

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

DATABASE = os.path.join(
    BASE_DIR,
    "database",
    "game_market_analysis.db"
)


def get_connection():
    return sqlite3.connect(DATABASE)