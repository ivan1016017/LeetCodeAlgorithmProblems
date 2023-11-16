import unittest
from src.my_project.interviews.top_150_questions.\
number_of_1_bits_updated_updated_updated_updated import Solution

class NumberOfOneBitsTestCase(unittest.TestCase):

    def test_number_of_one_bits(self):
        solution = Solution()
        output = solution.hammingWeight(n=4294967293)
        self.assertEqual(output,31)