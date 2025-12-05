import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_16_trapping_rain_water import Solution

class TrappingWaterTestCase(unittest.TestCase):

    def test_trapping_water_first_case(self):
        solution = Solution()
        output = solution.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1])
        target = 6
        self.assertEqual(output, target)

    def test_trapping_water_second_case(self):
        solution = Solution()
        output = solution.trap(height = [4,2,0,3,2,5])
        target = 9
        self.assertEqual(output, target)        