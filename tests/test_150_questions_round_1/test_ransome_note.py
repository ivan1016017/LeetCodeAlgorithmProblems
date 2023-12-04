import unittest
from src.my_project.interviews.top_150_questions_round_1.\
ransome_note import Solution

class RansomeNoteTestCase(unittest.TestCase):

    def test_ransome_note(self):
        solution = Solution()
        output = solution.canConstruct(ransomNote = "aa", magazine = "aab")
        self.assertTrue(output)

    def test_no_ransome_note(self):
        solution = Solution()
        output = solution.canConstruct(ransomNote = "a", magazine = "b")
        self.assertFalse(output)