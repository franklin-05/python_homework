import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Vector(Point):
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented


if __name__ == "__main__":
    p1 = Point(3, 4)
    p2 = Point(3, 4)
    p3 = Point(0, 0)
    print("Point 1:", p1)
    print("p1 == p2:", p1 == p2)
    print("Distance p1 to p3:", p1.distance(p3))

    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v1 + v2
    print("Vector 1:", v1)
    print("Vector 2:", v2)
    print("Vector Sum (v1 + v2):", v3)