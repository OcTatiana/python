import unittest

from generator import read_all_file
from generator import read_all_lines_from
from generator import merge_solutions
LEETCODE_END_LINK = '\n[comment]: <> (Stop)\n'

class Test_HexNumber(unittest.TestCase):
    def test_read_all_file(self):
        expect = "first name\n\n[comment]: <> (Stop)\n\nfirst solution"
        result = read_all_file("input.txt")
        self.assertEqual(expect, result)
    def test_read_all_lines(self):
        expect = ["first name\n", "\n", "[comment]: <> (Stop)\n", "\n", "first solution"]
        result = read_all_lines_from("input.txt")
        self.assertEqual(expect, result)
    def test_merge_solutions(self):
        expect = "first name\nsecond\nfirst solution"
        result = merge_solutions(read_all_file("input.txt"), "second")
        self.assertEqual(expect, result)



if __name__ == "__main__":
    unittest.main()
