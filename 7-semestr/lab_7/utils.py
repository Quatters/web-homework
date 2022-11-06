from sqlite3 import connect
from pathlib import Path


def get_db_connection():
    return connect(Path.cwd() / 'library.sqlite3')
