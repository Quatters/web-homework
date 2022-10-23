# импортируем необходимые модули
from jinja2 import Template
import sqlite3
import library_model


conn = sqlite3.connect("../library.sqlite3")
tables = {
    'publisher': library_model.get_publisher(conn),
    'genre': library_model.get_genre(conn),
    'reader': library_model.get_reader(conn),
    'author': library_model.get_author(conn),
    'book_author': library_model.get_book_author(conn),
    'book': library_model.get_book(conn),
    'book_reader': library_model.get_book_reader(conn),
}
conn.close()

f_template = open('library_templ.html')
html = f_template.read()
f_template.close()

template = Template(html)
result_html = template.render(
    tables=tables,
    len = len,
)

f = open('library.html', 'w', encoding ='utf-8-sig')
f.write(result_html)
f.close()
