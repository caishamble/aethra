import math

class Vector(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f})"

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, int):
            return Vector(self.x * other, self.y * other)


    def __rmul__(self, other):
        return self.__mul__(other)

    def magnitude(self):
        return round(math.sqrt(self.x ** 2 + self.y ** 2), 2)

    def unit(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot convert zero vector to a unit vector")
        self.x /= mag
        self.y /= mag

