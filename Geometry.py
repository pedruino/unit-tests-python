# coding=utf-8
from math import sqrt


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash((self.start, self.end))


class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def shift(self, x, y):
        self.x += x
        self.y += y

    def __repr__(self):
        return "".join(["Point(", str(self.x), ",", str(self.y), ")"])

    def __str__(self):
        return "{}, {}".format(self.x, self.y)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash((self.x, self.y))

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __add__(self, point):
        return Vector(self.x + point.x, self.y + point.y)

    def __sub__(self, point):
        return self + -point

    @classmethod
    def distance(cls, v1, v2):
        # √[(xA − xB)2 + (yA − yB)2 + (zA − zB)2]
        return sqrt(pow(v1.x - v2.x, 2) + pow(v1.y - v2.y, 2))
