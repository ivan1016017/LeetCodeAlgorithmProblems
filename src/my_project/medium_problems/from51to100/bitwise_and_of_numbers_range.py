from typing import List 

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        
        p = 0
        while left != right:
            left >>= 1
            right >>= 1
            p += 1
        return left << p
        
solution = Solution()

print(solution.rangeBitwiseAnd(left = 5, right = 7))
print(solution.rangeBitwiseAnd(left = 0, right = 0))
print(solution.rangeBitwiseAnd(left = 1, right = 2147483647))
