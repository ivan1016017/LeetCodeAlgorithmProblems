import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_52_min_stack import MinStack

class MinStackTestCase(unittest.TestCase):

    def test_first_pattern(self):
        commands = ["MinStack","push","push","push","getMin",
                    "pop","top","getMin"]
        args = [[],[-2],[0],[-3],[],[],[],[]]
        
        expected_output = [None,None,None,None,-3,None,0,-2]
        
        min_stack = None
        actual_output = []
        
        for i, command in enumerate(commands):
            if command == "MinStack":
                min_stack = MinStack()
                actual_output.append(None)
            elif command == "push":
                min_stack.push(args[i][0])
                actual_output.append(None)
            elif command == "pop":
                min_stack.pop()
                actual_output.append(None)
            elif command == "top":
                result = min_stack.top()
                actual_output.append(result)
            elif command == "getMin":
                result = min_stack.getMin()
                actual_output.append(result)
        
        self.assertEqual(actual_output, expected_output)

     