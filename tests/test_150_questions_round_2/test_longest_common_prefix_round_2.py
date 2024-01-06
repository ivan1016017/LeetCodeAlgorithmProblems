import unittest
from src.my_project.interviews.top_150_questions_round_2.\
longest_common_prefix import Solution

class LongestCommonPrefixTestCase(unittest.TestCase):

    def test_longes_common_prefix_empty_list(self):
        solution = Solution()
        output = solution.longestCommonPrefix(strs=[])
        self.assertEqual('',output)


    def test_longes_common_prefix_non_empty_list(self):
        solution = Solution()
        output = solution.longestCommonPrefix(strs = ["flower",
                                                      "flow",
                                                      "flight"])
        self.assertEqual("fl",output)

