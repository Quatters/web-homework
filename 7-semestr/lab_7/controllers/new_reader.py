from app import app
from flask import render_template


@app.route('/new_reader', methods=['get'])
def new_reader():
    return render_template('new_reader.html')
