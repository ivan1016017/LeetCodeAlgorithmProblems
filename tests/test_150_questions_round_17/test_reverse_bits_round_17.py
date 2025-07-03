import unittest
from src.my_project.interviews.top_150_questions_round_17\
.reverse_bits import Solution

class ReverseBitsTestCase(unittest.TestCase):

    def test_reverse_bits(self):
        solution = Solution()
        output = solution.reverseBits(2)
        target = 1073741824
        self.assertEqual(output, target)