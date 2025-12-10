import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_24_text_justification import Solution

class TextJustificationTestCase(unittest.TestCase):

    def test_first_pattern(self):
        solution = Solution()
        output = solution.fullJustify(words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16)
        target = [
   "This    is    an",
   "example  of text",
   "justification.  "
]

        self.assertEqual(output, target)

    def test_second_pattern(self):
        solution = Solution()
        output = solution.fullJustify(words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16)
        target = [
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
        self.assertEqual(output, target)