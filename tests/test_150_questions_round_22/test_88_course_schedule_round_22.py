import unittest
from src.my_project.interviews.top_150_questions_round_22\
    .ex_88_course_schedule import Solution
from typing import Optional, List


class CourseScheduleTestCase(unittest.TestCase):

    def test_example_1(self):
        """
        Example 1:
        Input: numCourses = 2, prerequisites = [[1,0]]
        Output: true
        Explanation: There are a total of 2 courses to take. 
        To take course 1 you should have finished course 0. So it is possible.
        """
        solution = Solution()
        numCourses = 2
        prerequisites = [[1, 0]]
        expected = True
        
        result = solution.canFinish(numCourses, prerequisites)
        self.assertEqual(result, expected)

    def test_example_2(self):
        """
        Example 2:
        Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
        Output: false
        Explanation: There are a total of 2 courses to take. 
        To take course 1 you should have finished course 0, and to take course 0 
        you should also have finished course 1. So it is impossible.
        """
        solution = Solution()
        numCourses = 2
        prerequisites = [[1, 0], [0, 1]]
        expected = False
        
        result = solution.canFinish(numCourses, prerequisites)
        self.assertEqual(result, expected)

