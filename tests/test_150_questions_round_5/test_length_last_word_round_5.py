import unittest
from src.my_project.interviews.top_150_questions_round_5.\
length_last_word import Solution

class LengthOfLastWordTestCase(unittest.TestCase):

    def test_length_last_word(self):
        solution = Solution()
        target = 5
        output = solution.lengthOfLastWord(s="Hello World")
        self.assertEqual(target, output)