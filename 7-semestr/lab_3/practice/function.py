from jinja2 import Template
import matplotlib.pyplot as plt

def f(x):
    return x ** 3 - 6 * x ** 2 + x + 5

def create_pict(x, y):
    line = plt.plot(x, y)
    plt.setp(line, color="blue", linewidth=2)
    plt.gca().spines["left"].set_position("zero")
    plt.gca().spines["bottom"].set_position("zero")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.savefig("pict.jpg")
    return "pict.jpg"

a = -2
b = 6
n = 30
h = (abs(a) + abs(b)) / n
x_list = [a + (idx * h) for idx in range(n + 1)]
f_list = [f(x) for x in x_list]

f_template = open('function_template.html', 'r', encoding ='utf-8-sig')
html = f_template.read()
f_template.close()

template = Template(html)
template.globals["len"] = len

f = open('function.html', 'w', encoding ='utf-8-sig')

name_pict = create_pict(x_list, f_list)

result_html = template.render(x=x_list, y=f_list, pict=name_pict)
f.write(result_html)
f.close()
