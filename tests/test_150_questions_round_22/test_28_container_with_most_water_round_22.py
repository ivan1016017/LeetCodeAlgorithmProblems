import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_28_container_with_most_water import Solution

class ContainerWithMostWaterTestCase(unittest.TestCase):

    def test_first_pattern(self):
        solution = Solution()
        output = solution.maxArea(height = [1,8,6,2,5,4,8,3,7])
        target = 49 
        self.assertEqual(output, target)

    def test_second_pattern(self):
        solution = Solution()
        output = solution.maxArea(height = [1,1])
        target = 1
        self.assertEqual(output, target)