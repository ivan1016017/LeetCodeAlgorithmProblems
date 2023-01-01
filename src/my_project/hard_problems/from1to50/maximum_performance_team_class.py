from typing import List, Union
from abc import ABC, abstractmethod
import heapq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:


        h = []
        res = sSum = 0

        for e, s in sorted(zip(efficiency, speed), reverse=1):
            heapq.heappush(h, s)
            sSum += s
            if len(h) > k:
                sSum -= heapq.heappop(h)
            res = max(res, sSum * e)
        return res % (10**9 + 7)

class SolutionTwo:
    def maxPerformance(self, n, speed, efficiency, k):
        worker = []
        for i in range(n):
            worker.append([speed[i], efficiency[i]])
        worker.sort(cmp = self.cmp)
        import heapq
        total = 0
        heap = []
        res = 0
        for i in range(k):
            total += worker[i][0]
            minE = worker[i][1]
            heapq.heappush(heap, worker[i][0])
            res = max(res, total*minE)
        for i in range(k, n):
            if worker[i][0] > heap[0]:
                total += (-heap[0]+worker[i][0])
                minE = worker[i][1]
                res = max(res, minE*total)
                heapq.heappop(heap)
                heapq.heappush(heap, worker[i][0])
        return res%1000000007
        
    def cmp(self, w1, w2):
        if w1[1] > w2[1]:
            return -1
        elif w1[1] == w2[1]:
            return 0
        else:
            return 1