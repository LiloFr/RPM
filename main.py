# RPM
from math import sqrt
a, b, c = float(input()), float(input()), float(input())
D = b ** 2 - (4 * a * c)
if D < 0:
    print('Нет корней')
elif D > 0:
    x1, x2 = (-b + sqrt(D)) / (2 * a), (-b - sqrt(D)) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))
elif D == 0:
    print(-b / (2 * a))
