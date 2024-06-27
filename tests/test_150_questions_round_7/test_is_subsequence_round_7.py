import unittest
from src.my_project.interviews.top_150_questions_round_7.\
is_subsequence import Solution

class IsSubsequenceTestCase(unittest.TestCase):

    def test_is_subsequence(self):
        solution = Solution()
        output = solution.isSubsequence(s="abc", t="ahbgdc")
        self.assertTrue(output)


    def test_is_no_subsequence(self):
        solution = Solution()
        output = solution.isSubsequence(s="axc", t="ahbgdc")
        self.assertFalse(output)
