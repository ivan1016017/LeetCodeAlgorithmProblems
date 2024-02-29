import unittest
from src.my_project.interviews.top_150_questions_round_3.\
reverse_bits import Solution

class ReverseBitTestCase(unittest.TestCase):

    def test_reverse_bits(self):
        solution = Solution()
        output = solution.reverseBits(2)
        self.assertEqual(1073741824, output)