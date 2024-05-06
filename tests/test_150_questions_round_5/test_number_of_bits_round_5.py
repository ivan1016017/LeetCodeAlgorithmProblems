import unittest
from src.my_project.interviews.top_150_questions_round_5.\
number_of_bits import Solution

class NumberOfBitsTestCase(unittest.TestCase):

    def test_number_of_bits(self):
        solution = Solution()
        output = solution.hammingWeight(n=2)
        target = 1
        self.assertEqual(target, output)

def sample1():
    pass 