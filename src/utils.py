import os

import psycopg
from dotenv import load_dotenv
import time
from psycopg import OperationalError

APP_ROOT = os.path.join(os.path.dirname(__file__), "..")
dotenv_path = os.path.join(APP_ROOT, ".env")

load_dotenv(dotenv_path)


def get_database():
    conn = None
    while True:
        try:
            conn = psycopg.connect(
                f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
            )
            break
        except OperationalError:
            print("Waiting for database to be ready...")
            time.sleep(3)
    return conn
