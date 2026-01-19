import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_53_evaluate_reverse_polish_notation import Solution

class EvaluateReversePolishNotationTestCase(unittest.TestCase):

    def test_first_pattern(self):
        solution = Solution()
        output = solution.evalRPN(tokens = ["2","1","+","3","*"])
        target = 9
        self.assertEqual(output, target)

    def test_second_pattern(self):
        solution = Solution()
        output = solution.evalRPN(tokens = ["4","13","5","/","+"])
        target =  6
        self.assertEqual(output, target)

    def test_third_pattern(self):
        solution = Solution()
        output = solution.evalRPN(tokens = ["10","6","9","3","+","-11",
                                            "*","/","*","17","+","5","+"])
        target =  22
        self.assertEqual(output, target)        