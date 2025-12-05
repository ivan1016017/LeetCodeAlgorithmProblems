import unittest 
from src.my_project.interviews.top_150_questions_round_22\
.ex_15_candy import Solution

class CandyTestCase(unittest.TestCase):

    def test_candy_first_case(self):
        solution = Solution()
        output = solution.candy(ratings = [1,0,2])
        target = 5 
        self.assertEqual(output, target)

    def test_candy_second_case(self):
        solution = Solution()
        output = solution.candy(ratings = [1,2,2])
        target = 4 
        self.assertEqual(output, target)        