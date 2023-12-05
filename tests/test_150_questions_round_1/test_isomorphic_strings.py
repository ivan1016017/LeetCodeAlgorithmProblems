import unittest
from src.my_project.interviews.top_150_questions_round_1.\
isomorphic_strings import Solution

class IsomorphicStringTestCase(unittest.TestCase):

    def test_isomorphic_strings(self):
        solution = Solution()
        output = solution.isIsomorphic(s = "egg", t = "add")
        self.assertTrue(output)

    def test_no_isomorphic_strings(self):
        solution = Solution()
        output = solution.isIsomorphic(s = "foo", t = "bar")
        self.assertFalse(output)