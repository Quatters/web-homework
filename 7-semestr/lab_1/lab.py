import os
from sqlite3 import connect
from pandas import read_sql
from pprint import pprint

DB_PATH = f'{os.path.dirname(os.path.abspath(__file__))}/mydb.sqlite3'

if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

connection = connect(DB_PATH)
cursor = connection.cursor()

cursor.executescript("""
    CREATE TABLE publisher(
        publisher_id INTEGER PRIMARY KEY AUTOINCREMENT,
        publisher_name VARCHAR(255)
    );

    INSERT INTO publisher (publisher_name) VALUES
    ('ЭКСМО'),
    ('ДРОФА'),
    ('АСТ');

    CREATE TABLE genre(
        genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
        genre_name VARCHAR(255)
    );

    INSERT INTO genre (genre_name) VALUES
    ('Роман'),
    ('Приключения'),
    ('Детектив'),
    ('Поэзия'),
    ('Фантастика'),
    ('Фэнтези');

    CREATE TABLE book(
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(255),
        genre_id INTEGER,
        publisher_id INTEGER,
        year_publication INTEGER,
        available_numbers INTGER,

        CONSTRAINT book_publisher_fk
        FOREIGN KEY (publisher_id) REFERENCES publisher(publisher_id),

        CONSTRAINT book_genre_fk
        FOREIGN KEY (genre_id) REFERENCES genre(genre_id)
    );

    INSERT INTO book (
        title,
        genre_id,
        publisher_id,
        year_publication,
        available_numbers
    ) VALUES
    ('Мастер и Маргарита', 1, 2, 2014, 5),
    ('Таинственный остров', 2, 2, 2015, 10),
    ('Бородино', 4, 3, 2015, 12),
    ('Дубровский', 1, 2, 2020, 7),
    ('Вокруг света за 80 дней', 2, 2, 2019, 5),
    ('Убийства по алфавиту', 1, 1, 2017, 9),
    ('Затерянный мир', 2, 1, 2020, 3),
    ('Герой нашего времени', 1, 3, 2017, 2),
    ('Смерть поэта', 4, 1, 2020, 2),
    ('Поэмы', 4, 3, 2019, 5);
""")
connection.commit()

print("""
1. Вывести книги (указать их жанр), количество которых принадлежит интервалу
от a до b, включая границы (границы интервала передать в качестве параметра).
""")

cursor.execute("""
    SELECT title, genre_name
    FROM book
    JOIN genre ON genre.genre_id = book.genre_id
    WHERE available_numbers BETWEEN :min AND :max;
""", {'min': 5, 'max': 8})

pprint(cursor.fetchall())
print('\n')

print("""
2. Вывести книги (указать их издательство), название которой состоит из одного
слова, и книга издана после заданного года (год передать в качестве параметра).
""")

cursor.execute("""
    SELECT title, publisher_name
    FROM book
    JOIN publisher ON publisher.publisher_id = book.publisher_id
    WHERE title NOT LIKE '% %' AND year_publication > :year;
""", {'year': 2015})

pprint(cursor.fetchall())
print('\n')

print("""
3. Вычислить, сколько экземпляров книг каждого жанра представлены в библиотеке.
Учитывать только книги, изданные после заданного года (год передать в качестве
параметра).
""")

cursor.execute("""
    SELECT genre_name, Sum(available_numbers)
    FROM book
    JOIN genre ON genre.genre_id = book.genre_id
    WHERE year_publication > :year
    GROUP BY book.genre_id
""", {'year': 2019})

pprint(cursor.fetchall())
print('\n')

print("""
Отобрать информацию о книгах, количество которых больше 3. Столбцы назвать
Книга, Жанр, Издательство и Количество.
Вывести отобранную информацию:
- в виде таблицы;
- только столбец Название;
- 3-ю строку результата запроса;
- количество строк и столбцов в результате запроса;
- названия столбцов.
""")

result = read_sql("""
    SELECT title AS Книга, genre_name AS Жанр,
        publisher_name AS Издательство, available_numbers AS Количество
    FROM book
    JOIN publisher on publisher.publisher_id = book.publisher_id
    JOIN genre on genre.genre_id = book.genre_id
    WHERE available_numbers > 3;
""", connection)

print(result, '\n')
print(result['Книга'], '\n')
print(result.loc[3], '\n')
print('Кол-во строк:', result.shape[0], '\n')
print('Кол-во столбцов:', result.shape[1], '\n')
print(result.dtypes.index, '\n')

print("""
1. Создать кортеж, в который включить название двух издательств. Реализовать
запрос, который выводит книги издательств, входящих в кортеж, изданных с 2016
по 2019 года, включая границы.
""")

genre_list = ('Поэзия', 'Роман')
result = read_sql(f"""
    SELECT title AS Книга, genre_name AS Жанр, publisher_name AS Издательство,
        available_numbers AS Количество, year_publication AS Год
    FROM book
    JOIN publisher on publisher.publisher_id = book.publisher_id
    JOIN genre on genre.genre_id = book.genre_id
    WHERE genre_name in {genre_list} AND
    year_publication BETWEEN 2016 AND 2019;
""", connection)

print(result)

connection.close()
