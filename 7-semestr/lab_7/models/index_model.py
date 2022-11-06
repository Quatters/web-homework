import pandas
from sqlite3 import Connection
from datetime import date


def get_reader(conn):
    return pandas.read_sql('''
        SELECT * FROM reader
    ''', conn)


def get_book_reader(conn, reader_id):
    return pandas.read_sql('''
        WITH get_authors(book_id, authors_name)
        AS(
            SELECT book_id, GROUP_CONCAT(author_name)
            FROM author JOIN book_author USING(author_id)
            GROUP BY book_id
        )
        SELECT
            title AS Название,
            authors_name AS Авторы,
            borrow_date AS Дата_выдачи,
            return_date AS Дата_возврата,
            book_reader_id
        FROM reader
        JOIN book_reader USING(reader_id)
        JOIN book USING(book_id)
        JOIN get_authors USING(book_id)
        WHERE reader.reader_id = :id
        ORDER BY 3
    ''', conn, params={"id": reader_id})


# для обработки данных о новом читателе
def get_new_reader(conn: Connection, new_reader):
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO reader (reader_name)
        VALUES (:new_reader)
    """, {'new_reader': new_reader})
    conn.commit()
    return cur.lastrowid


def borrow_book(conn: Connection, book_id, reader_id):
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO book_reader (book_id, reader_id, borrow_date, return_date)
        VALUES (:book_id, :reader_id, date(), NULL)
    """, {'book_id': book_id, 'reader_id': reader_id})
    cur.execute("""
        UPDATE book
        SET available_numbers = available_numbers - 1
        WHERE book_id = :book_id
    """, {'book_id': book_id})
    conn.commit()


def return_book(conn: Connection, book_reader_id, reader_id):
    cur = conn.cursor()
    cur.execute("""
        UPDATE book
        SET available_numbers = available_numbers + 1
        WHERE book_id = (
            SELECT book_id
            FROM book_reader
            WHERE book_reader_id = :book_reader_id
        )
    """, {'book_reader_id': book_reader_id})
    cur.execute("""
        UPDATE book_reader
        SET return_date = :date
        WHERE book_reader_id = :book_reader_id
    """, {'book_reader_id': book_reader_id, 'date': date.today()})
    conn.commit()
