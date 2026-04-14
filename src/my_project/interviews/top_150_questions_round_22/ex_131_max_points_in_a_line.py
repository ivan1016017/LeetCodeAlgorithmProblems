from math import gcd
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        result = 2
        for i in range(n):
            slopes = {}
            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                g = gcd(dx, dy)
                dx //= g
                dy //= g
                if dx < 0:
                    dx, dy = -dx, -dy
                elif dx == 0:
                    dy = abs(dy)
                slopes[(dx, dy)] = slopes.get((dx, dy), 0) + 1
            if slopes:
                result = max(result, max(slopes.values()) + 1)
        return result