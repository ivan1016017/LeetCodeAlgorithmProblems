import unittest
from src.my_project.interviews.top_150_questions_round_19\
.remove_element import Solution

class RemoveElementTestCase(unittest.TestCase):

    def test_remove_element(self):
        solution = Solution()
        output = solution.removeElement(nums=[3,2,2,3], val=3)
        target = 2
        self.assertEqual(output, target)