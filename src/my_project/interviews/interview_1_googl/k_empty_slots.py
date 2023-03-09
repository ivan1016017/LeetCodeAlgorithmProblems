from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
import bisect


class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        intervals = [] # [1,7] -> [1,6,7] -> [1,5,6,7] -> [1,4,5,6,7] (search with binary search and check the difference with idx + 1 and idx - 1)
        
        for i in range(len(bulbs)):
            idx = bisect.bisect(intervals, bulbs[i])
            intervals.insert(idx, bulbs[i])
            if idx - 1 >= 0 and intervals[idx] - intervals[idx - 1] - 1 == k:
                return i + 1
            elif idx + 1 < len(intervals) and intervals[idx + 1] - intervals[idx] - 1 == k:
                return i + 1
            
        return -1