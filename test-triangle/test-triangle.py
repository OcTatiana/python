import sys


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def Side(self, a, b):
        return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5

    def isTriangle(self):
        s1 = self.Side(self.a, self.b)
        s2 = self.Side(self.b, self.c)
        s3 = self.Side(self.c, self.a)

        if s1 + s2 <= s3:
            return False
        elif s2 + s3 <= s1:
            return False
        elif s3 + s1 <= s2:
            return False
        else:
            return True

    def isIsosceles(self):
        s1 = self.Side(self.a, self.b)
        s2 = self.Side(self.b, self.c)
        s3 = self.Side(self.c, self.a)

        if s1 == s2 or s2 == s3 or s3 == s1:
            return True
        else:
            return False

    def Square(self):
        return 0.5 * abs((self.b.x - self.a.x) * (self.c.y - self.a.y) - (self.c.x - self.a.x) * (self.b.y - self.a.y))


import unittest


class TestTriangle(unittest.TestCase):
    def test_isTriangle(self):
        p1 = Point(1, 1)
        p2 = Point(0, 0)
        p3 = Point(2, 0)
        T = Triangle(p1, p2, p3)
        self.assertEqual(True, T.isTriangle(), "T is not triangle")

    def test_isIsosceles(self):
        p1 = Point(1, 1)
        p2 = Point(0, 0)
        p3 = Point(2, 0)
        T = Triangle(p1, p2, p3)
        self.assertEqual(True, T.isIsosceles(), "T is not Isosceles")

    def test_Square(self):
        p1 = Point(1, 1)
        p2 = Point(0, 0)
        p3 = Point(2, 0)
        T = Triangle(p1, p2, p3)
        self.assertEqual(1, T.Square(), "The area is considered incorrectly")


def main():
    unittest.main()


if __name__ == "__main__":
    main()
