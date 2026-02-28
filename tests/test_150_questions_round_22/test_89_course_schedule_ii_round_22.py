import unittest
from src.my_project.interviews.top_150_questions_round_22\
    .ex_89_course_schedule_ii import Solution
from typing import Optional, List


class CourseScheduleIITestCase(unittest.TestCase):

    def is_valid_order(self, numCourses: int, prerequisites: List[List[int]], order: List[int]) -> bool:
        """Helper function to validate if an order satisfies all prerequisites."""
        if len(order) != numCourses:
            return False
        
        # Create position map
        position = {course: i for i, course in enumerate(order)}
        
        # Check if all prerequisites are satisfied
        for course, prereq in prerequisites:
            if position[prereq] >= position[course]:
                return False
        
        return True

    def test_example_1(self):
        """
        Example 1:
        Input: numCourses = 2, prerequisites = [[1,0]]
        Output: [0,1]
        Explanation: There are a total of 2 courses to take. 
        To take course 1 you should have finished course 0. 
        So the correct course order is [0,1].
        """
        solution = Solution()
        numCourses = 2
        prerequisites = [[1, 0]]
        
        result = solution.findOrder(numCourses, prerequisites)
        self.assertTrue(self.is_valid_order(numCourses, prerequisites, result))

    def test_example_2(self):
        """
        Example 2:
        Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
        Output: [0,2,1,3]
        Explanation: There are a total of 4 courses to take. 
        To take course 3 you should have finished both courses 1 and 2. 
        Both courses 1 and 2 should be taken after you finished course 0.
        So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
        """
        solution = Solution()
        numCourses = 4
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        
        result = solution.findOrder(numCourses, prerequisites)
        self.assertTrue(self.is_valid_order(numCourses, prerequisites, result))

    def test_example_3(self):
        """
        Example 3:
        Input: numCourses = 1, prerequisites = []
        Output: [0]
        """
        solution = Solution()
        numCourses = 1
        prerequisites = []
        expected = [0]
        
        result = solution.findOrder(numCourses, prerequisites)
        self.assertEqual(result, expected)

