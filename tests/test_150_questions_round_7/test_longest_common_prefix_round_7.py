import unittest
from src.my_project.interviews.top_150_questions_round_7.\
longest_common_prefix import Solution

class LongestCommonPrefixTestCase(unittest.TestCase):

    def test_empty(self):
        solution = Solution()
        output = solution.longestCommonPrefix(strs=[])
        target = '' 
        self.assertEqual(output, target)

    def test_non_common_prefix(self):
        solution = Solution()
        output = solution.longestCommonPrefix(strs=["dog","racecar","car"])
        target = '' 
        self.assertEqual(output, target)

    def test_longest_common_prefix(self):
        solution = Solution()
        output = solution.longestCommonPrefix(strs=["flower","flow","flight"])
        target = "fl"
        self.assertEqual(output, target)