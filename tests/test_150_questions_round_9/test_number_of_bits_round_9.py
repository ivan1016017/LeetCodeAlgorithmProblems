import unittest
from my_project.interviews.top_150_questions_round_9\
.number_of_one_bits import Solution

class NumberOfOnesTestCase(unittest.TestCase):

    def test_number_of_ones(self):
        solution = Solution()
        output = solution.hammingWeight(n=11)
        target = 3
        self.assertEqual(output, target)