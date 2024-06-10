import unittest
from src.my_project.interviews.top_150_questions_round_6.\
number_of_one_bits import Solution

class NumberOfOneBitsTestCase(unittest.TestCase):

    def test_number_of_one_bits(self):
        solution = Solution()
        output = solution.hammingWeight(n=11)
        target = 3 
        self.assertEqual(output, target)