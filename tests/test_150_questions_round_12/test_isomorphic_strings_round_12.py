import unittest
from src.my_project.interviews.top_150_questions_round_12\
.isomorphic_strings import Solution


class IsomorphicStringsTestCase(unittest.TestCase):

    def test_are_isomorphic_strings(self):
        solution = Solution()
        output = solution.isIsomorphic(s="egg", t="add")
        self.assertTrue(output)

    def test_are_not_isomorphic_strings(self):
        solution = Solution()
        output = solution.isIsomorphic(s="foo", t="bar")
        self.assertFalse(output)
