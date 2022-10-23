import os
import sqlite3
from pathlib import Path
from jinja2 import Template
from model import get_books, get_author, get_genre, get_publisher


DIRNAME = Path(__file__).parent

reader_id = 6

applied_filters = {
    'author_id': [1],
    'genre_id': [1, 2],
    # 'publisher_id': []
}

with sqlite3.connect(Path(DIRNAME.parent / 'library.sqlite3')) as connection:
    df = get_books(connection, applied_filters)
    df_genre = get_genre(connection)
    df_author = get_author(connection)
    df_publisher = get_publisher(connection)

html = (DIRNAME / 'template.html').read_text()


template = Template(html)
result_html = template.render(
    len=len,
    df=df,
    filters={
        'Жанр': df_genre,
        'Автор': df_author,
        'Издательство': df_publisher,
    },
    applied_filters=applied_filters,
)

(DIRNAME / 'result.html').write_text(result_html)
