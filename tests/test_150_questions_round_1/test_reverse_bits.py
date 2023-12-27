import unittest
from src.my_project.interviews.top_150_questions_round_1.\
reverse_bits import Solution

class ReverseBitsTestCase(unittest.TestCase):

    def test_reverse_bits(self):
        solution = Solution()
        output = solution.reverseBits(n=2)
        self.assertEqual(1073741824, output)