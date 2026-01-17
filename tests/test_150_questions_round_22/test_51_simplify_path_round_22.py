import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_51_simplify_path import Solution

class SimplifyPathTestCase(unittest.TestCase):

    def test_first_pattern(self):
        solution = Solution()
        output = solution.simplifyPath("/home/")
        target = "/home"
        self.assertEqual(output, target)

    def test_second_pattern(self):
        solution = Solution()
        output = solution.simplifyPath(path = "/home//foo/")
        target =  "/home/foo"
        self.assertEqual(output, target)

    def test_third_pattern(self):
        solution = Solution()
        output = solution.simplifyPath(path = "/.../a/../b/c/../d/./")
        target =  "/.../b/d"
        self.assertEqual(output, target)        