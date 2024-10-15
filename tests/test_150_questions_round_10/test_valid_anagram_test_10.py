import unittest
from src.my_project.interviews.top_150_questions_round_10\
.valid_anagram import Solution

class ValidAnagramTestCase(unittest.TestCase):

    def test_is_valid_anagram(self):
        solution = Solution()
        output = solution.isAnagram(s="anagram", t="nagaram")
        self.assertTrue(output)


    def test_is_no_valid_anagram(self):
        solution = Solution()
        output = solution.isAnagram(s="rat", t="car")
        self.assertFalse(output)