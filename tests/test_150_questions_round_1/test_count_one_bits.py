import unittest
from src.my_project.interviews.top_150_questions_round_1.\
count_one_bits import Solution

class CountOneBitsTestCase(unittest.TestCase):

    def test_count_one_bits(self):
        solution = Solution()
        output = solution.hammingWeight(n=5)
        self.assertEqual(2,output)