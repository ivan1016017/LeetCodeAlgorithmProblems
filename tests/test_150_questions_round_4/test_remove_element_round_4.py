import unittest
from src.my_project.interviews.top_150_questions_round_4.\
remove_element import Solution

class RemoveElementTestCase(unittest.TestCase):

    def test_remove_element(self):
        solution = Solution()
        output = solution.removeElement(nums=[1,2,2], val=2)
        self.assertEqual(1, output)