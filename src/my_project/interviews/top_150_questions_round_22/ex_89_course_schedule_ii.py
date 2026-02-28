from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build adjacency list and in-degree array
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        # Initialize queue with courses that have no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        result = []
        
        # Process courses in topological order
        while queue:
            course = queue.popleft()
            result.append(course)
            
            # Reduce in-degree for dependent courses
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        # If we processed all courses, return the order; otherwise return empty list
        return result if len(result) == numCourses else []