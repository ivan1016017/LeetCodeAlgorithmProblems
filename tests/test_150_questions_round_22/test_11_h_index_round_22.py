import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_11_h_index import Solution

class hIndexTestCase(unittest.TestCase):

    def test_h_index_test_1(self):
        solution = Solution()
        output = solution.hIndex(citations = [3,0,6,1,5])
        target = 3
        self.assertEqual(output, target)

    def test_h_index_test_2(self):
        solution = Solution()
        output = solution.hIndex(citations = [1,3,1])
        target = 1
        self.assertEqual(output, target)        