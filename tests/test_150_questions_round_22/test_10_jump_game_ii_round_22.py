import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_10_jump_game_ii import Solution

class JumpIITestCase(unittest.TestCase):

    def test_jump_i_first_case(self):
        solution = Solution()
        output = solution.jump(nums = [2,3,1,1,4])
        target = 2 
        self.assertEqual(output, target)

    def test_jump_i_second_case(self):
        solution = Solution()
        output = solution.jump(nums = [2,3,0,1,4])
        target = 2 
        self.assertEqual(output, target)        
