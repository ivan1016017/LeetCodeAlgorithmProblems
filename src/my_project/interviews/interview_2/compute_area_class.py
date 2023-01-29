from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        width = min(ax2,bx2) - max(ax1,bx1) 
        height = min(ay2,by2) - max(ay1,by1)
        overlap = 0 if width <= 0 or height <= 0 else width*height
        return (ax2-ax1)*(ay2-ay1) + (bx2-bx1)*(by2-by1) - overlap

        