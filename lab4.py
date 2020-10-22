#библиотека для дифференцирования
from sympy import *

#бибилиотеки для построения графиков
import matplotlib.pyplot as plt
import numpy

#Задаем функцию
def func(x):
    return (x ** 5) - 7 * (x ** 3) + 8 * (x ** 2) - 2 * x

#Рисуем график
xlist = list(numpy.arange(-5, 5, 0.01))
ylist = list(map(func, xlist))
plt.plot(xlist, ylist)
plt.ylim(-5, 5)
plt.grid()
plt.title('(x ** 5) - 7 * (x ** 3) + 8 * (x ** 2) - 2 * x')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.show()

#Значения х, находящиеся рядом с нулевыми значениями функции, добавляем в список val
val = []
x = -10
while x <= 10:
    if func(x + 0.1) * func(x - 0.1) < 0:
        val.append(round(x, 1))
        x += 0.1
    x += 0.1
print(val)


otv = []
for i in val:
    f = True
    a = i + 0.1
    b = i - 0.1
    e = 1
    #Реализуем метод бисекции для поиска иксов в рамках погрешности е, иксы добавляем в список otv
    while e > 0.000001:
        x = (a + b) / 2
        if func(x) * func(a) < 0: b = x
        elif func(x) * func(b) < 0: a = x
        elif func(x) == 0: break
        e = abs(func(x))
    otv.append(x)
print(otv)

#Реализуем модифицированный метод Ньютона
otv = []
for i in val:
    x = symbols('x')
    #производная функции в точке x = i
    func_diff = diff(func(x), x).evalf(subs={'x':i})
    x = i
    while abs((func(x))) > 0.000001:
        x = x - (func(x)) / func_diff
    otv.append(x)
print(otv)