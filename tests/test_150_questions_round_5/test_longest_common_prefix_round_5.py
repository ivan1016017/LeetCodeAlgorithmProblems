import unittest
from src.my_project.interviews.top_150_questions_round_5.\
longest_common_prefix import Solution

class LongestCommonPrefixTestCase(unittest.TestCase):

    def test_longest_common_prefix_non_empty(self):
        solution = Solution()
        target = 'fl'
        output = solution.longestCommonPrefix(strs=["flower","flow","flight"])
        self.assertEqual(target, output)

    def test_longest_common_prefix_empty(self):
        solution = Solution()
        target = ''
        output = solution.longestCommonPrefix(strs=["a","b","c"])
        self.assertEqual(target, output)

def sample_remove():
    print('testing removing')