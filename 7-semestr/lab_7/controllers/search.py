from app import app
from flask import render_template, request
from models.search_model import (
    get_author,
    get_books,
    get_genre,
    get_publisher,
)
from utils import get_db_connection


@app.route('/search', methods=['get'])
def search():
    conn = get_db_connection()
    applied_filters = {
        'genre_id': list(map(int, request.values.getlist('genre_id'))),
        'author_id': list(map(int, request.values.getlist('author_id'))),
        'publisher_id': list(map(int, request.values.getlist('publisher_id'))),
    }
    return render_template(
        'search.html',
        filters={
            'Жанр': get_genre(conn),
            'Автор': get_author(conn),
            'Издательство': get_publisher(conn),
        },
        df=get_books(conn, applied_filters),
        len=len,
        applied_filters=applied_filters,
    )
