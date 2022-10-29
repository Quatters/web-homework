from asyncio import constants
from app import app
from flask import render_template
from constants import programs, subjects, olympiads


@app.route('/', methods=['GET'])
def index():
    return render_template(
        'index.html',
        program_list=programs,
        subject_list=subjects,
        olympiad_list=olympiads,
        len=len
    )
