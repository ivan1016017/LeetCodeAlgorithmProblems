import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_09_jump_game_i import Solution

class JumpITestCase(unittest.TestCase):

    def test_jump_i_first_case_true(self):
        solution = Solution()
        output = solution.canJump(nums = [2,3,1,1,4])
        self.assertTrue(output)

    def test_jump_i_first_case_false(self):
        solution = Solution()
        output = solution.canJump(nums = [3,2,1,0,4])    
        self.assertFalse(output)        