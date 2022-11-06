from app import app
from flask import render_template, request, session
from utils import get_db_connection
from models.index_model import (
    get_reader,
    get_book_reader,
    get_new_reader,
    borrow_book,
    return_book,
)


@app.route('/', methods=['get', 'post'])
def index():
    conn = get_db_connection()

    if (reader_id := request.values.get('reader_id')):
        reader_id = int(reader_id)
        session['reader_id'] = reader_id
    elif (new_reader := request.values.get('new_reader')):
        new_reader = new_reader
        session['reader_id'] = get_new_reader(conn, new_reader)
    elif (book_id := request.values.get('book_id')):
        book_id = int(book_id)
        borrow_book(conn, book_id, session['reader_id'])
    else:
        session['reader_id'] = 1

    if (return_id := request.values.get('return')):
        return_id = int(return_id)
        return_book(conn, return_id, session['reader_id'])

    df_reader = get_reader(conn)
    df_book_reader = get_book_reader(conn, session['reader_id'])

    return render_template(
        'index.html',
        reader_id=session['reader_id'],
        combo_box=df_reader,
        book_reader=df_book_reader,
        len=len,
    )
