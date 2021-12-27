# Добрый день! Базовый класс - вектор. У него методы определения длины, арифметическин операции.
# На его основе класс прямоугольник. Необходимо найти площадь полученного прямоугольника.
# Не каждая четверка векторов может давать прямоугольник
from math import *


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector [{self.x}, {self.y}]'

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, k):
        return Vector(self.x * k, self.y * k)

    def lenVector(self):
        return int(sqrt(self.x ** 2 + self.y ** 2))


class Rectangle(Vector):
    def __init__(self, a, b, c, d, aRoute, bRoute, cRoute, dRoute):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.aRoute = aRoute
        self.bRoute = bRoute
        self.cRoute = cRoute
        self.dRoute = dRoute

    def s(self):
        return self.a * self.b

    def check(self):
        if self.a == self.c and self.b == self.d and self.aRoute[1] == self.bRoute[0] and self.bRoute[1] == \
                self.cRoute[0] and self.cRoute[1] == self.dRoute[0] and self.dRoute[1] == self.aRoute[
            0]:
            print('Cтороны подходят! Проверка прошла успешно!')
            print('Площадь прямоугольника:', r.s())
        else:
            print('Стороны не подходят,нужны другие')


v1 = Vector(10, 5)
v2 = Vector(10, 5)  # длины
v3 = Vector(4, 5)
v4 = Vector(4, 5)

a = [[1, 7], [1, 5]]
b = [[1, 5], [2, -2]]  # координаты
c = [[2, -2], [-3, 4]]
d = [[-3, 4], [1, 7]]

r = Rectangle(v1.lenVector(), v3.lenVector(), v2.lenVector(), v4.lenVector(), a, b, c, d)

print('Векторы:', v1, v2, v3, v4)
print('Сложение первого и второго:', v1 + v2)
print('Вычитание второго и третьего:', v2 - v3)
print('Умножение второго на число:', v2 * 3)
print()
print('Длина вектора', v1.lenVector())
print('Длина вектора', v2.lenVector())
print('Длина вектора', v3.lenVector())
print('Длина вектора', v4.lenVector())
print()
r.check()
