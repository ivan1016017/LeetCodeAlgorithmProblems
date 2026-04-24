import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_141_interleaving_string import Solution


class InterleavingStringTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertTrue(self.solution.isInterleave("aabcc", "dbbca", "aadbbcbcac"))

    def test_example2(self):
        self.assertFalse(self.solution.isInterleave("aabcc", "dbbca", "aadbbbaccc"))

    def test_empty_strings(self):
        self.assertTrue(self.solution.isInterleave("", "", ""))

    def test_wrong_length(self):
        self.assertFalse(self.solution.isInterleave("a", "b", "abc"))

    def test_one_empty(self):
        self.assertTrue(self.solution.isInterleave("", "abc", "abc"))
        self.assertTrue(self.solution.isInterleave("abc", "", "abc"))