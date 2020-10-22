
from sympy import *

x, y = symbols('x y')

#Система уравнений
f1 = (x + y) * (x ** 2 - y ** 2) - 16
f2 = (x - y) * (x ** 2 + y ** 2) - 40

#Диффернцируем обе функции по х и по у
f1x, f1y = diff(f1, x), diff(f1, y)
f2x, f2y = diff(f2, x), diff(f2, y)

#Находим определители
d = f1x * f2y - f2x * f1y
dx = f1 * f2y - f2 * f1y
dy = f1x * f2 - f2x * f1

xi, yi = -0.1, 0.5
e = 1
while e > 0.001:
    #фактические значения определителей
    dxi = dx.evalf(subs={'x':xi, 'y':yi})
    dyi = dy.evalf(subs={'x':xi, 'y':yi})
    di = d.evalf(subs={'x':xi, 'y':yi})
    #уточнение решения заданной системы
    xi = xi - dxi / di
    yi = yi - dyi / di
    e = max(dxi, dyi)

print(xi, yi)


