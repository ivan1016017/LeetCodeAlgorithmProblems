import unittest
from src.my_project.interviews.top_150_questions_round_19\
.longest_common_prefix import Solution

class LongestCommonPrefixTestCase(unittest.TestCase):

    def test_longest_common_prefix(self):
        solution = Solution()
        output = solution.longestCommonPrefix(strs=["flower","flow","flight"])
        target = 'fl'
        self.assertEqual(target, output)

    def test_longest_no_common_prefix(self):
        solution = Solution()
        output = solution.longestCommonPrefix(strs=["dog","racecar","car"])
        target = ''
        self.assertEqual(target, output)

    def test_longest_common_prefix_null_list(self):
        solution = Solution()
        output = solution.longestCommonPrefix(strs=[])
        target = ''
        self.assertEqual(target, output)