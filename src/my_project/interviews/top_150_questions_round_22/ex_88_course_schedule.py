from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, 
                        prerequisites: List[List[int]]) -> bool:
        # Build adjacency list and in-degree array
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        # Add all courses with no prerequisites to queue
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        courses_taken = 0
        
        # Process courses
        while queue:
            course = queue.popleft()
            courses_taken += 1
            
            # Reduce in-degree for dependent courses
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        # If we took all courses, no cycle exists
        return courses_taken == numCourses