import pandas as pd


def get_reader(conn) -> pd.DataFrame:
    return pd.read_sql('SELECT * FROM reader', conn)


def get_book_reader(conn, reader_id) -> pd.DataFrame:
    return pd.read_sql("""
        SELECT
        	title AS 'Название',
        	group_concat(DISTINCT author_name) AS 'Авторы',
        	borrow_date AS 'Дата выдачи',
        	return_date AS 'Дата возврата'
        FROM book
        JOIN book_reader USING(book_id)
        JOIN book_author USING(book_id)
        JOIN author USING(author_id)
        WHERE reader_id = :reader_id
        GROUP BY book_id
    """, conn, params={'reader_id': reader_id})
