import unittest
from src.my_project.interviews.top_150_questions_round_1.\
longest_common_prefix import Solution


class LongestCommonPrefixTestCase(unittest.TestCase):

    def test_null_list(self):
        solution = Solution()
        output = solution.longestCommonPrefix(strs=[])
        self.assertEqual(output,"")

    def test_non_null_list(self):
        solution = Solution()
        output = solution.longestCommonPrefix(
                                            strs = ["flower","flow","flight"])
        self.assertEqual(output,"fl")