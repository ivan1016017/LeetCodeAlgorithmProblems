import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_22_zig_zag import Solution

class ZigZagTestCase(unittest.TestCase):

    def test_first_pattern(self):
        solution = Solution()
        output = solution.convert(s = "PAYPALISHIRING", numRows = 3)
        target = "PAHNAPLSIIGYIR"
        self.assertEqual(target, output)

    def test_second_pattern(self):
        solution = Solution()
        output = solution.convert(s = "A", numRows = 1)
        target = "A"
        self.assertEqual(target, output)

