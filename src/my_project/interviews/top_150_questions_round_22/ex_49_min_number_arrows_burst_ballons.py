from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # Sort balloons by end coordinate
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        current_arrow_pos = points[0][1]
        
        for i in range(1, len(points)):
            # If current balloon starts after the last arrow position,
            # we need a new arrow
            if points[i][0] > current_arrow_pos:
                arrows += 1
                current_arrow_pos = points[i][1]
        
        return arrows        