import unittest
from src.my_project.interviews.top_150_questions_round_4.\
length_of_last_word import Solution

class LengthOfLastWordTestCase(unittest.TestCase):

    def test_length_of_last_word(self):
        solution = Solution()
        output = solution.lengthOfLastWord(s="Hello World")
        self.assertEqual(5, output)
