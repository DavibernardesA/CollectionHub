from src.utils import get_database

DATABASE = get_database()


def get_cursor():
    return DATABASE.cursor()
