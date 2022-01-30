from typing import List 
import math

class Solution:

    def numSquares(self, n: int) -> int:
        s = [i*i for i in range(1,int(math.sqrt(n))+1)] # Square numbers <= n
        l = 0  # BFS level
        currentLevel = [0]  # List of numbers in BFS level l

        while True:
            nextLevel = []
            for a in currentLevel:
                for b in s:
                    if a+b == n: 
                        return l+1  # Found n
                    if a+b < n:  nextLevel.append(a+b)
            currentLevel = list(set(nextLevel))  # Remove duplicates
            l += 1