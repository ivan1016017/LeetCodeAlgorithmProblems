import unittest
from src.my_project.interviews.top_150_questions_round_6.\
add_binary import Solution

class AddBinaryTestCase(unittest.TestCase):

    def test_add_binary(self):
        solution = Solution()
        target = "100"
        output = solution.addBinary(a="11", b="1")
        self.assertEqual(output, target)
        