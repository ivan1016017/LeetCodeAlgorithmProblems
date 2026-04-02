import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Min-heap of (capital_required, profit) sorted by capital
        min_cap_heap = sorted(zip(capital, profits))
        cap_idx = 0
        # Max-heap of profits (negate for max behavior)
        max_profit_heap = []

        for _ in range(k):
            # Push all affordable projects into the max-profit heap
            while cap_idx < len(min_cap_heap) and min_cap_heap[cap_idx][0] <= w:
                heapq.heappush(max_profit_heap, -min_cap_heap[cap_idx][1])
                cap_idx += 1

            if not max_profit_heap:
                break

            w += -heapq.heappop(max_profit_heap)

        return w
