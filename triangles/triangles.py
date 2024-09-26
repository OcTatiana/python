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
        s1 = self.Side(self.a, self.b)
        s2 = self.Side(self.b, self.c)
        s3 = self.Side(self.c, self.a)
        p = (s1 + s2 + s3) / 2
        return (p * (p - s1) * (p - s2) * (p - s3)) ** 0.5


class File:
    def __init__(self, filename):
        self.filename = filename

    def get_all_lines(self):
        file = open(self.filename, 'r')
        result = file.readlines()
        file.close()
        return result

    def write_result(self, string):
        file = open(self.filename, 'w')
        file.write(string)
        file.close()


def Parsing(arr):
    if len(arr) != 6:
        return False
    else:
        return True


def main():
    name_input_file = sys.argv[1]
    name_output_file = sys.argv[2]

    res = []
    input = File(name_input_file)
    lines = input.get_all_lines()

    if lines:
        for line in lines:
            crd = line.split(" ")
            if Parsing(crd):
                x1, y1, x2, y2, x3, y3 = (
                    int(crd[0]), int(crd[1]), int(crd[2]), int(crd[3]), int(crd[4]), int(crd[5]))
                A = Point(x1, y1)
                B = Point(x2, y2)
                C = Point(x3, y3)
                T = Triangle(A, B, C)
                if T.isTriangle() and T.isIsosceles():
                    res.append(T.Square())
                else:
                    res.append(-1)

        output = File(name_output_file)
        i = res.index(max(res))
        if max(res) != -1:
            output.write_result(lines[i])


if __name__ == "__main__":
    main()
