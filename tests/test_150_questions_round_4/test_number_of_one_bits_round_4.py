import unittest
from src.my_project.interviews.top_150_questions_round_4.\
number_of_one_bits import Solution

class NumberOfOneBitsTestCase(unittest.TestCase):

    def test_number_of_one_bits(self):
        solution = Solution()
        n = 11
        target = 3
        output = solution.hammingWeight(n=n)
        self.assertEqual(target,output)
