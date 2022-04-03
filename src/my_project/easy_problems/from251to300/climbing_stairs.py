class Solution:
    def climbStairs(self, n: int) -> int:
        
        a, b = 1, 1
        for i in range(n):
            a, b = a, a+b 
        return a