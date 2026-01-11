import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_42_group_anagrams import Solution

class GroupAnagramsTestCase(unittest.TestCase):

    def test_first_pattern(self):
        solution = Solution()
        output = solution.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"])
        target = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        self.assertEqual(output, target)

    def test_second_pattern(self):
        solution = Solution()
        output = solution.groupAnagrams(strs = [""])
        target = [[""]]
        self.assertEqual(output, target)

    def test_third_pattern(self):
        solution = Solution()
        output = solution.groupAnagrams(strs = ["a"])
        target = [["a"]]
        self.assertEqual(output, target)