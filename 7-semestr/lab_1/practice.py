import os
from sqlite3 import connect
from pandas import read_sql

CWD = os.path.dirname(os.path.abspath(__file__))
DB_PATH = f'{CWD}/library.sqlite3'
DUMP_PATH = f'{CWD}/library.db'

connection = connect(DB_PATH)

with open(DUMP_PATH,'r', encoding='utf-8-sig') as f:
    connection.executescript(f.read())
    connection.commit()

print("""
1. Для каждого жанра посчитать, сколько различных книг этого жанра представлено
в библиотеке, каково общее количество доступных экземпляров книг (имеющихся в
наличии) и какой самый ранний год издания книг, относящихся к этому жанру.
Информацию отсортировать по названию жанра в алфавитном порядке.
""")

result = read_sql("""
    SELECT
        genre_name AS Жанр,
        count(book_id) AS 'Различных книг',
        sum(available_numbers) AS 'Общее кол-во',
        min(year_publication) AS 'Самое ранее издание'
    FROM book
    JOIN genre on book.genre_id = genre.genre_id
    GROUP BY book.genre_id
    ORDER BY genre.genre_name
""", connection)

print(result, '\n')

print("""
2. Вывести информацию о всех книгах, который сдал заданный читатель. Для каждой
книги указать дату выдачи, дату сдачи и сколько дней книга была на руках.
Информацию отсортировать по убыванию количества дней (В SQLite нет функции
DATEDIFF, самостоятельно найти способ реализации этой функции).
""")

result = read_sql("""
    SELECT
        title AS Книга,
        borrow_date AS 'Дата выдачи',
        return_date AS 'Дата сдачи',
        cast(julianday(return_date) - julianday(borrow_date) AS INTEGER)
            AS 'Дней на руках'
    FROM book
    JOIN book_reader ON book_reader.book_id = book.book_id
    JOIN reader ON reader.reader_id = book_reader.reader_id
    WHERE reader_name = :reader_name
    ORDER BY 'Была на руках' DESC
""", connection, params={'reader_name': 'Абрамова А.А.'})

print(result, '\n')

print("""
3. Вывести самый популярный жанр (жанры). Самым популярным считается жанр,
книги которого чаще всего брали читатели в библиотеке. Вывести название жанра
(жанров) и сколько раз читатели брали книги этого жанра. Информацию
отсортировать по названию жанров в алфавитном порядке.
""")

result = read_sql("""
    SELECT
        genre_name AS Жанр ,
        max(_count) AS 'Взято, раз'
    FROM (
        SELECT genre_name, count(book_id) as _count
        FROM book
        JOIN genre ON genre.genre_id = book.genre_id
        GROUP BY genre.genre_id
    ) AS subquery
    ORDER BY genre_name
""", connection)

print(result, '\n')

print("""
1. Вывести книги, которые были взяты в библиотеке в октябре месяце. Указать
фамилии читателей, которые их взяли, а также дату, когда их взяли. Столбцы
назвать Название, Читатель, Дата соответственно. Информацию отсортировать
сначала по возрастанию даты, потом в алфавитном порядке по фамилиям читателей,
и, наконец, по названиям книг тоже в алфавитном порядке.
""")

result = read_sql("""
    SELECT
        title AS Название,
        reader_name AS Читатель,
        borrow_date AS Дата
    FROM book
    JOIN book_reader ON book.book_id = book_reader.book_id
    JOIN reader ON reader.reader_id = book_reader.reader_id
    WHERE borrow_date LIKE '%-10-%'
    ORDER BY borrow_date DESC, reader_name, title
""", connection)

print(result, '\n')

print("""
2. Для каждой книги, изданной в заданном издательстве, вывести информацию о ее
принадлежности к группе:
- если книга издана раньше 2014 года, вывести "III";
- если книга издана в период с 2014 года по 2017 год, вывести "II";
- если книга издана позже 2017 года, вывести "I".
Для каждой книги также указать ее жанр и год издания. Столбцы назвать
Название, Жанр, Год, Группа. Информацию отсортировать сначала по группе в
порядке убывания, потом возрастанию года издания и, наконец, по названию в
алфавитном порядке.
""")

result = read_sql("""
    SELECT
        title AS Книга,
        genre_name AS Жанр,
        year_publication AS Год,
        CASE
            WHEN year_publication < 2014 THEN 'III'
            WHEN year_publication BETWEEN 2014 AND 2017 THEN 'II'
            WHEN year_publication > 2017 THEN 'I'
        END AS Группа
    FROM book
    JOIN publisher ON book.publisher_id = publisher.publisher_id
    JOIN genre ON book.genre_id = genre.genre_id
    ORDER BY Группа DESC, year_publication, title
""", connection, params={'publisher_name': 'ЭКСМО'})

print(result, '\n')

print("""
4. Для каждой книги вывести количество экземпляров, которые есть в наличии
(available_numbers) в библиотеке, а также сколько раз экземпляры книги брали
читатели. Если книгу читатели не брали - вывести 0. Столбцы назвать Название,
Количество, Количество_выдачи. Информацию отсортировать сначала по убыванию
количества выданных экземпляров, а потом по названию книги в алфавитном порядке
и, наконец, по возрастанию доступного количества.
""")

result = read_sql("""
    SELECT
        title AS Название,
        available_numbers AS Количество,
        count(book_reader.book_id) AS Количество_выдачи
    FROM book
    LEFT JOIN book_reader ON book_reader.book_id = book.book_id
    GROUP BY book.book_id
    ORDER BY Количество_выдачи DESC, title, available_numbers
""", connection)

print(result)

connection.close()
