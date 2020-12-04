#библиотека для параметризации функции и построения графиков
from sympy import *

#библиотека для вычисления факториала
import math

#функция
x = symbols('x')
y = (x - 1) ** 6
print(y)

#массив (список) опорных точек
xi = [1, 1.25, 1.5, 1.75, 2]
print(xi)

def interp(y, xi):
    #создаем список для записи значений функции и конечных разностей
    dy = [[] for i in range(len(xi))]
    #записываем в список значения функции в каждой из опорных точек
    for i in xi: dy[0].append(y.evalf(subs={'x':i}))
    #заполнение списка значениями конечных разностей
    for j in range(0, len(dy) - 1):
        for i in range(len(dy[j]) - 1):
            dy[j + 1].append(dy[j][i + 1] - dy[j][i])

    #вычисляем многочлен
    def multi(n):
        mul = 1
        for j in range(n):
            mul *= (x - xi[j])
        return mul

    f = dy[0][0]
    for i in range(1, len(xi)):
        f += dy[i][0] * multi(i)/ (math.factorial(i) * (xi[1] - xi[0]) ** i)

    return f

#значение многочлена в точке 1.7
print(interp(y, xi).evalf(subs={'x':1.7}))

#поиск погрешности
max = 0
xn = xi[0]
xmax = xn
while xn < xi[len(xi) - 1]:
    t = abs(interp(y, xi).evalf(subs={'x':xn}) - y.evalf(subs={'x':xn}))
    if t > max:
        max = t
        xmax = xn
    xn += 0.01
print(max, xmax, interp(y, xi).evalf(subs={'x':xmax}), y.evalf(subs={'x':xmax}))

#графики исходной функции и интерполяционного многочлена в одних осях
p = plot(y, (x, 1, 2), line_color = 'r', show = False)
p.extend(plot(interp(y, xi), (x, 1, 2), show = False))
p.show()
