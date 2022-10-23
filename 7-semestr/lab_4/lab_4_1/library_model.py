import pandas as pd


def get_publisher(conn):
    return pd.read_sql("SELECT * FROM publisher", conn)


def get_genre(conn):
    return pd.read_sql("SELECT * FROM genre", conn)


def get_reader(conn):
    return pd.read_sql("SELECT * FROM reader", conn)


def get_author(conn):
    return pd.read_sql("SELECT * FROM author", conn)


def get_book_author(conn):
    return pd.read_sql("SELECT * FROM book_author", conn)


def get_book(conn):
    return pd.read_sql("SELECT * FROM book", conn)


def get_book_reader(conn):
    return pd.read_sql("SELECT * FROM book_reader", conn)
