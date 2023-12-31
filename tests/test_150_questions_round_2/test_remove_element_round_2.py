import unittest
from src.my_project.interviews.top_150_questions_round_2.\
remove_element import Solution

class RemoveElementTestCase(unittest.TestCase):
    
    def test_remove_element(self):
        solution = Solution()
        output = solution.removeElement(nums=[1,1,2,3,4,5],
                                        val=1)
        self.assertEqual(4, output)