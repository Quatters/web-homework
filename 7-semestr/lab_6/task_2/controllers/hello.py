from asyncio import constants
from app import app
from flask import render_template, request
from constants import programs, subjects, olympiads


@app.route('/hello', methods=['GET'])
def hello():
    name = request.values.get('username', '')
    gender = request.values.get('gender', '')
    program_id = int(request.values.get('program', 0))
    subject_ids = request.values.getlist('subject[]')
    subjects_select = [subjects[int(i)] for i in subject_ids]
    olympiad_ids = request.values.getlist('olympiad[]')
    olympiads_select = [olympiads[int(i)] for i in olympiad_ids]

    return render_template(
        'hello.html',
        name=name,
        gender=gender,
        program=programs[program_id],
        program_list=programs,
        subjects_select=subjects_select,
        subject_list=subjects,
        olympiads_select=olympiads_select,
        olympiads=olympiads,
        len=len,
    )
