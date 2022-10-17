from jinja2 import Template
from pathlib import Path


student = [
    [
        "Алина",
        "Бизнес-информатика",
        ["Базы данных", "Программирование", "Статистика"],
        "ж",
    ],
    [
        "Вадим",
        "Экономика",
        ["Информатика", "Теория игр", "Статистика"],
        "м",
    ],
    [
        "Ксения",
        "Экономика",
        ["Информатика", "Теория игр", "Статистика"],
        "ж"
    ]
]

html = (Path.cwd() / 'test_template.html').read_text(encoding='utf-8')
ind_html = (Path.cwd() / 'ind_test_template.html').read_text(encoding='utf-8')

def add_spaces(text):
    return " ".join(text)

def get_disciplines(num):
    if num % 10 == 1:
        return f'{num} дисциплину'
    elif num % 10 in (2, 3, 4):
        return f'{num} дисциплины'
    else:
        return f'{num} дисциплин'


template = Template(html)
template.globals['len'] = len
template.globals['add_spaces'] = add_spaces
result_html = template.render(user=student[2])
(Path.cwd() / 'test.html').write_text(result_html)

template = Template(ind_html)
template.globals['len'] = len
template.globals['add_spaces'] = add_spaces
template.globals['get_disciplines'] = get_disciplines
result_html = template.render(user=student[2])
(Path.cwd() / 'ind_test.html').write_text(result_html)
