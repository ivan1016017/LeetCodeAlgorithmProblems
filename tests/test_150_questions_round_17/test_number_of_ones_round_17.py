import unittest
from src.my_project.interviews.top_150_questions_round_17\
.number_of_ones import Solution

class NumberOfOnesTestCase(unittest.TestCase):

    def test_number_of_ones(self):
        solution = Solution()
        output = solution.hammingWeight(n=11)
        target = 3
        self.assertEqual(output, target)
