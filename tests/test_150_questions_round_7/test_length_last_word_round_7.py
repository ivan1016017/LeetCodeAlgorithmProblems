import unittest
from src.my_project.interviews.top_150_questions_round_7.\
length_last_word import Solution

class LengthOfLastWord(unittest.TestCase):

    def test_length_last_word(self):
        solution = Solution()
        output = solution.lengthOfLastWord(s="Hello World")
        target = 5
        self.assertEqual(output, target)