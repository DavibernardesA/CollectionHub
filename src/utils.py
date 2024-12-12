import os

import psycopg
from dotenv import load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__), "..")
dotenv_path = os.path.join(APP_ROOT, ".env")

load_dotenv(dotenv_path)

conn = psycopg.connect(
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
)

cursor = conn.cursor()
