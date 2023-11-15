import unittest
from src.my_project.interviews.top_150_questions.\
reverse_bits_updated_updated_updated_updated import Solution

class ReverseBitsTestCase(unittest.TestCase):

    def test_check_reverse_bits(self):
        solution = Solution()
        output = solution.reverseBits(n=4294967293)
        self.assertEqual(output,3221225471)
