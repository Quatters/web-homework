from jinja2 import Template
import matplotlib.pyplot as plt

def f_x(x, n_var):
    if n_var == 0:
        y = x ** 3 - 6 * x ** 2 + x + 5
    elif n_var == 1:
        y = x ** 2 - 5 * x + 1
    elif n_var == 2:
        y = 1 / (x ** 2 + 1)
    return y

def create_pict(x, y):
    line = plt.plot(x, y)
    plt.setp(line, color="blue", linewidth=2)
    plt.gca().spines["left"].set_position("zero")
    plt.gca().spines["bottom"].set_position("zero")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.savefig("pict.jpg")
    return "pict.jpg"

n_var = 1
list_f = ["f(x)", "y(x)", "z(x)"]

a = -10
b = 10
n = 100
h = (abs(a) + abs(b)) / n
x_list = [a + (idx * h) for idx in range(n + 1)]
f_list = [f_x(x, n_var) for x in x_list]

f_template = open('function_template2.html', 'r', encoding ='utf-8-sig')
html = f_template.read()
f_template.close()

template = Template(html)
template.globals["len"] = len

f = open('function2.html', 'w', encoding ='utf-8-sig')

name_pict = create_pict(x_list, f_list)

result_html = template.render(
    x=x_list,
    y=f_list,
    pict=name_pict,
    n_var=n_var,
    list_f=list_f,
    a=a,
    b=b,
    n=n,
    x_list=x_list,
    f_list=f_list,
)
f.write(result_html)
f.close()
