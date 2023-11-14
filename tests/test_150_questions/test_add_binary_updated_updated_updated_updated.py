import unittest
from src.my_project.interviews.top_150_questions.\
add_binary_updated_updated_updated_updated import Solution

class AddBinaryTestCase(unittest.TestCase):

    def test_binary_sum(self):
        solution = Solution()
        output = solution.addBinary(a='11',b='1')
        self.assertEqual(output,'100')