import unittest
from src.my_project.interviews.top_150_questions_round_5.\
single_number import Solution

class SingleNumberTestCase(unittest.TestCase):

    def test_single_number(self):
        solution = Solution()
        output = solution.singleNumber(nums=[2,2,1])
        target = 1
        self.assertEqual(target, output)

def sample1():
    print('test1')