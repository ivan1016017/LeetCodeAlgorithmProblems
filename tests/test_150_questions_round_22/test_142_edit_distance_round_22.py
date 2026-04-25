import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_142_edit_distance import Solution


class EditDistanceTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.minDistance("horse", "ros"), 3)

    def test_example2(self):
        self.assertEqual(self.solution.minDistance("intention", "execution"), 5)

    def test_empty_word1(self):
        self.assertEqual(self.solution.minDistance("", "abc"), 3)

    def test_empty_word2(self):
        self.assertEqual(self.solution.minDistance("abc", ""), 3)

    def test_both_empty(self):
        self.assertEqual(self.solution.minDistance("", ""), 0)

    def test_same_words(self):
        self.assertEqual(self.solution.minDistance("abc", "abc"), 0)

    def test_single_insert(self):
        self.assertEqual(self.solution.minDistance("a", "ab"), 1)

    def test_single_replace(self):
        self.assertEqual(self.solution.minDistance("a", "b"), 1)