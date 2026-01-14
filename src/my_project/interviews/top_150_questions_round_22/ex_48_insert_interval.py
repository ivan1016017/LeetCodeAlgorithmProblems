from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def insert(self, 
               intervals: List[List[int]], 
               newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)

        answer = []

        for i in sorted(intervals, key=lambda x: x[0]):

            if answer and i[0] <= answer[-1][-1]:
                answer[-1][-1] = max(i[-1],answer[-1][-1])
            else:
                answer.append(i)

        return answer 

