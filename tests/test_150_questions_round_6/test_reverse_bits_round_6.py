import unittest
from src.my_project.interviews.top_150_questions_round_6.\
reverse_bits import Solution

class ReverseBitsTestCase(unittest.TestCase):

    def test_reverse_bits(self):
        solution = Solution()
        output = solution.reverseBits(n=5)
        target = 2684354560
        self.assertEqual(output, target)