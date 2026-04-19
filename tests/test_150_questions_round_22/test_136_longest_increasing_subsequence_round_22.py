import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_136_longest_increasing_subsequence import Solution


class IncreasingLongestSubquenceTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]), 4)

    def test_example2(self):
        self.assertEqual(self.solution.lengthOfLIS([0, 1, 0, 3, 2, 3]), 4)

    def test_example3(self):
        self.assertEqual(self.solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]), 1)

    def test_single_element(self):
        self.assertEqual(self.solution.lengthOfLIS([5]), 1)


if __name__ == '__main__':
    unittest.main()
