from typing import List 
from abc import ABC, abstractmethod
import heapq


class MedianFinder:
    """
    Find median from data stream using two heaps:
    - max_heap: stores the smaller half (negated for max behavior)
    - min_heap: stores the larger half
    
    Invariants:
    1. max_heap size >= min_heap size
    2. max_heap size - min_heap size <= 1
    3. All elements in max_heap <= all elements in min_heap
    """

    def __init__(self):
        self.max_heap = []  # stores smaller half (negated values)
        self.min_heap = []  # stores larger half

    def addNum(self, num: int) -> None:
        # Always add to max_heap first (negated)
        heapq.heappush(self.max_heap, -num)
        
        # Move the largest from max_heap to min_heap
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        
        # Balance: max_heap should have same or 1 more element than min_heap
        if len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        