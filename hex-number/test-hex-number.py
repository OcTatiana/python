import unittest
from hexnumber import HexNumber

def list_in_string(num):
    a = num.num
    number = ""
    while a is not None:
        number += a.val
        a = a.next
    if number[-1] == '0':
        number = number[:-1:1]
    return number


class Test_HexNumber(unittest.TestCase):
    def test_add1(self):
        num1 = HexNumber("1111")
        num2 = HexNumber("2222")
        expect = list_in_string(HexNumber("3333"))
        result = list_in_string(num1.add(num2))
        self.assertEqual(expect, result)

    def test_add2(self):
        num1 = HexNumber("1111")
        num2 = HexNumber("EEF")
        expect = list_in_string(HexNumber("2000"))
        result = list_in_string(num1.add(num2))
        self.assertEqual(expect, result)

    def test_add3(self):
        num1 = HexNumber("F7F")
        num2 = HexNumber("A3")
        expect = list_in_string(HexNumber("1022"))
        result = list_in_string(num1.add(num2))
        self.assertEqual(expect, result)

if __name__ == "__main__":
    unittest.main()
