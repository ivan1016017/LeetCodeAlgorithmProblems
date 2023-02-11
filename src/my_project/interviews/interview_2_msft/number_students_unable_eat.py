from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import defaultdict

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        temp_first_item: int = None

        while sandwiches[0] in students:

            if sandwiches[0] == students[0]:
                sandwiches.remove(sandwiches[0])
                students.remove(students[0])
                if sandwiches == students: 
                    return 0
            else: 
                temp_first_item  = students[0]
                students = students[1:] + [temp_first_item]

        return len(students)