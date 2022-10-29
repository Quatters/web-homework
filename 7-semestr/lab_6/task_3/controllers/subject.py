from app import app
from flask import render_template
from constants import subject_dict


@app.route('/subject/<sub>')
def subject(sub):
    return render_template(
        'subject.html',
        sub=sub,
        description=subject_dict[sub]
    )
