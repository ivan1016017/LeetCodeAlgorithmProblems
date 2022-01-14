from typing import List 
import collections


class Solution:
    def maxPoints(self, points):
        if len(points) <= 2: return len(points)
        d = collections.defaultdict(int) # slope : count
        result = 0
        for i in range(len(points)):
            d.clear()
            overlap, curmax = 0, 0
            for j in range(i+1, len(points)):
                dx, dy = points[j][0] - points[i][0], points[j][1] - points[i][1]
                if dx == 0 and dy == 0:
                    overlap += 1
                    continue
                slope = dy * 1.0 / dx if dx != 0 else 'infinity'
                d[slope] += 1
                curmax = max(curmax, d[slope])
            result = max(result, curmax+overlap+1)
        return result