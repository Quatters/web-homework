from app import app
from flask import render_template
from constants import olympiad_dict


@app.route('/olympiad/<olymp>')
def olympiad(olymp):
    return render_template(
        'olympiad.html',
        olymp=olymp,
        description=olympiad_dict[olymp]
    )
