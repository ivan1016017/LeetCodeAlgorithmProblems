import unittest
from src.my_project.interviews.top_150_questions_round_3.\
longest_common_prefix import Solution

class LongestCommonPrefixTestCase(unittest.TestCase):

    def test_longest_common_prefix(self):
        solution = Solution()
        output = solution.longestCommonPrefix(strs=["flower","flow","flight"])
        self.assertEqual('fl', output)

    def test_no_longest_common_prefix(self):
            solution = Solution()
            output = solution.longestCommonPrefix(strs=["a","b","c"])
            self.assertEqual('', output)

    def test_empty(self):
                solution = Solution()
                output = solution.longestCommonPrefix(strs=[])
                self.assertEqual('', output)