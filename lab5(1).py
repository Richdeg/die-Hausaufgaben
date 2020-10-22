
from sympy import *

x, y, z = symbols('x y z')

#Система уравнений
f1 = x * y + y * z - 8
f2 = y * z + z * x - 9
f3 = z * x + x * y - 5

#Диффернцируем обе функции по х и по у
f1x, f1y, f1z = diff(f1, x), diff(f1, y), diff(f1, z)
f2x, f2y, f2z = diff(f2, x), diff(f2, y), diff(f2, z)
f3x, f3y, f3z = diff(f3, x), diff(f3, y), diff(f3, z)

#Находим определители
d = (f1x * f2y * f3z) + (f1y * f2z * f3x) + (f2x * f3y * f1z) - (f3x * f2y * f1z) - (f2x * f1y * f3z) - (f2z * f3y * f1x)
dx = (f1 * f2y * f3z) + (f1y * f2z * f3) + (f2 * f3y * f1z) - (f3 * f2y * f1z) - (f2 * f1y * f3z) - (f2z * f3y * f1)
dy = (f1x * f2 * f3z) + (f1 * f2z * f3x) + (f2x * f3 * f1z) - (f3x * f2 * f1z) - (f2x * f1 * f3z) - (f2z * f3 * f1x)
dz = (f1x * f2y * f3) + (f1y * f2 * f3x) + (f2x * f3y * f1) - (f3x * f2y * f1) - (f2x * f1y * f3) - (f2 * f3y * f1x)

xi, yi, zi = 0.5, 0.5, 0.5
e = 1
while e > 0.01:
    #фактические значения определителей
    dxi = dx.evalf(subs={'x':xi, 'y':yi, 'z':zi})
    dyi = dy.evalf(subs={'x':xi, 'y':yi, 'z':zi})
    dzi = dz.evalf(subs={'x': xi, 'y': yi, 'z': zi})
    di = d.evalf(subs={'x':xi, 'y':yi, 'z':zi})
    #уточнение решения заданной системы
    xi = xi - dxi / di
    yi = yi - dyi / di
    zi = zi - dzi / di
    e = max(dxi, dyi, dzi)

print(xi, yi, zi)