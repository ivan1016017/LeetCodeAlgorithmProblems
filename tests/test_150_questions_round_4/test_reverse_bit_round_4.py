import unittest
from src.my_project.interviews.top_150_questions_round_4.\
reverse_bits import Solution

class ReverseBitTestCase(unittest.TestCase):

    def test_reverse_bits(self):
        solution = Solution()
        output = solution.reverseBits(n=7)
        target = 3758096384
        self.assertEqual(target, output)
