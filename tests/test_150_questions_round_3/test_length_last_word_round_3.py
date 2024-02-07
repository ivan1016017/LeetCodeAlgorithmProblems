import unittest 
from src.my_project.interviews.top_150_questions_round_3.\
length_last_word import Solution

class LengthLastWord(unittest.TestCase):

    def test_length_last_word(self):
        solution = Solution()
        output = solution.lengthOfLastWord(s="Hello World")
        self.assertEqual(5, output)