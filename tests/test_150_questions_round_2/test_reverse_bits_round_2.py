import unittest
from src.my_project.interviews.top_150_questions_round_2.\
reverse_bits import Solution

class ReverseBits(unittest.TestCase):

    def test_reverse_bits(self):
        solution = Solution()
        output = solution.reverseBits(2)
        self.assertEqual(1073741824, output)