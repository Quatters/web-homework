from pandas import read_sql


def get_genre(connection):
    return read_sql('SELECT * FROM genre', connection)


def get_author(connection):
    return read_sql('SELECT * FROM author', connection)


def get_publisher(connection):
    return read_sql('SELECT * FROM publisher', connection)


def format_filters(filters: dict, keys):
    _filters = filters.copy()
    for key in keys:
        _filters[key] = ','.join([str(x) for x in _filters.get(key, [])])
    return _filters


def get_books(connection, applied_filters=None):
    applied_filters = format_filters(
        applied_filters or {},
        ['genre_id', 'author_id', 'publisher_id']
    )
    genres = applied_filters['genre_id']
    publishers = applied_filters['publisher_id']
    authors = applied_filters['author_id']

    return read_sql(f"""
        SELECT
            book_id,
        	title AS 'Название',
        	group_concat(DISTINCT author_name) AS 'Авторы',
        	genre_name AS 'Жанр',
        	publisher_name AS 'Издательство',
            year_publication AS 'Год_издания',
            available_numbers AS 'Количество'
        FROM book
        JOIN genre USING(genre_id)
        JOIN publisher USING(publisher_id)
        JOIN book_author USING(book_id)
        JOIN author USING(author_id)
        GROUP BY book_id
        HAVING (genre_id IN ({genres}) OR {not genres})
            AND (publisher_id IN ({publishers}) OR {not publishers})
            AND (author_id IN ({authors}) OR {not authors})
        ORDER BY
            title,
            available_numbers DESC,
            genre_name,
            year_publication DESC
    """, connection)
