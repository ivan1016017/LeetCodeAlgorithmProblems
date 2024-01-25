import unittest 
from src.my_project.interviews.top_150_questions_round_2.\
count_one_bits import Solution

class CountOneBitsTestCase(unittest.TestCase):

    def test_count_one_bits(self):
        solution = Solution()
        output = solution.hammingWeight(5)
        self.assertEqual(2, output)