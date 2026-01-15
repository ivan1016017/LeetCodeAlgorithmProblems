import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_49_min_number_arrows_burst_ballons import Solution

class ArrowsBurstBallonsTestCase(unittest.TestCase):

    def test_first_pattern(self):
        solution = Solution()
        output = solution.findMinArrowShots(points = [[10,16],[2,8],[1,6],[7,12]])
        target = 2
        self.assertEqual(output, target)

    def test_second_pattern(self):
        solution = Solution()
        output = solution.findMinArrowShots(points = [[1,2],[3,4],[5,6],[7,8]])
        target = 4
        self.assertEqual(output, target)

    def test_third_pattern(self):
        solution = Solution()
        output = solution.findMinArrowShots(points = [[1,2],[2,3],[3,4],[4,5]])
        target = 2
        self.assertEqual(output, target)        