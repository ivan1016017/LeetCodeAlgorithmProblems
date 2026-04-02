import unittest
from typing import List
from src.my_project.interviews.top_150_questions_round_22\
    .ex_117_ipo import Solution


class IPOTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """k=2, w=0, profits=[1,2,3], capital=[0,1,1] -> 4"""
        self.assertEqual(self.solution.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]), 4)

    def test_example_2(self):
        """k=3, w=0, profits=[1,2,3], capital=[0,1,2] -> 6"""
        self.assertEqual(self.solution.findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]), 6)

    def test_no_affordable_projects(self):
        """Initial capital too low for all projects -> w unchanged"""
        self.assertEqual(self.solution.findMaximizedCapital(2, 0, [5, 10], [3, 5]), 0)

    def test_k_larger_than_projects(self):
        """k exceeds number of projects, should pick all"""
        self.assertEqual(self.solution.findMaximizedCapital(10, 0, [1, 2, 3], [0, 0, 0]), 6)

    def test_single_project_affordable(self):
        """Only one project affordable"""
        self.assertEqual(self.solution.findMaximizedCapital(1, 1, [5, 10], [1, 100]), 6)

    def test_large_initial_capital(self):
        """Enough capital to start any project, always pick highest profit"""
        self.assertEqual(self.solution.findMaximizedCapital(2, 10, [3, 7, 5], [0, 0, 0]), 22)

    def test_all_same_capital_requirement(self):
        """All projects have same capital requirement"""
        self.assertEqual(self.solution.findMaximizedCapital(2, 0, [4, 2, 6], [0, 0, 0]), 10)

    def test_k_is_zero(self):
        """k=0, no projects selected"""
        self.assertEqual(self.solution.findMaximizedCapital(0, 5, [1, 2, 3], [0, 0, 0]), 5)


if __name__ == '__main__':
    unittest.main()
