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
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def s(self):
        return self.a * self.b

    def find_coordinatesAB(self):
        coordinates = []
        for i in range(2):
            coordinates.append(self.b[i] - (self.a[i]))

        return coordinates

    def find_coordinatesCD(self):
        coordinates = []
        for i in range(2):
            coordinates.append(self.d[i] - (self.c[i]))
            # print(d[i],c[i])
            # print(coordinates)

        return coordinates

    def find_coordinatesAD(self):
        coordinates = []
        for i in range(2):
            coordinates.append(self.d[i] - (self.a[i]))

        return coordinates

    def find_coordinatesBC(self):
        coordinates = []
        for i in range(2):
            coordinates.append(self.c[i] - (self.b[i]))

        return coordinates


def find_lengthAB(AB):
    len = sqrt(AB[0] ** 2 + AB[1] ** 2)
    return len


def find_lengthCD(CD):
    len = sqrt(CD[0] ** 2 + CD[1] ** 2)
    return len


def find_lengthAD(AD):
    len = sqrt(AD[0] ** 2 + AD[1] ** 2)
    return len


def find_lengthBC(BC):
    len = sqrt(BC[0] ** 2 + BC[1] ** 2)
    return len


def check(lenAB, lenCD):
    if lenAB == lenCD:
        return True


# a = [0, -3]
# b = [-1, 0]
# c = [5, 2]
# d = [6, -1]

a = [0, 0]
b = [0, 2]
c = [4, 2]
d = [4, 0]

r = Rectangle(a, b, c, d)
a = Vector(a[0], a[1])
b = Vector(b[0], b[1])

AB = r.find_coordinatesAB()
CD = r.find_coordinatesCD()
AD = r.find_coordinatesAD()
BC = r.find_coordinatesBC()
# print(AB, CD, AD, BC)

lenAB = find_lengthAB(AB)
lenCD = find_lengthCD(CD)
lenAD = find_lengthAD(AD)
lenBC = find_lengthBC(BC)
# print(lenAB, lenCD, lenAD, lenBC)

if check(lenAB, lenCD):
    print('стороны AB и CD параллельны и равны')
    if sqrt(lenAD ** 2 + lenCD ** 2) == sqrt(lenAB ** 2 + lenBC ** 2):
        print('Диагонали равны! это прямоугольник!')

print('Длина вектора', a.lenVector())
print('Cложение векторов:', a.__add__(b))
print('Вектор: ', a.__repr__())
#print('Длина вектора', v.__sub__())
