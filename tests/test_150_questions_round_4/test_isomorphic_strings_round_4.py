import unittest
from src.my_project.interviews.top_150_questions_round_4.\
isomorphic_strings import Solution

class IsomorphicStrings(unittest.TestCase):

    def test_is_isomorphic(self):
        solution = Solution()
        output = solution.isIsomorphic(s="egg", t="add")
        self.assertTrue(output)

    def test_is_no_isomorphic(self):
        solution = Solution()
        output = solution.isIsomorphic(s="foo", t="bar")
        self.assertFalse(output)