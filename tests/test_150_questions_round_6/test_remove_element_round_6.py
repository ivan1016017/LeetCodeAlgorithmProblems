import unittest
from src.my_project.interviews.top_150_questions_round_6.\
remove_element import Solution

class RemoveElementsTestCase(unittest.TestCase):

    def test_remove_elements(self):
        solution = Solution()
        output = solution.removeElement(nums=[3,2,2,3], val=3)
        target = 2
        return self.assertEqual(target, output)