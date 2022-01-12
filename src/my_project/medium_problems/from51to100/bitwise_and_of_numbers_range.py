from typing import List 

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        temp = 0
        if left == 0:
            return 0
        
        if left == right: 
            return right
        
        if left < right:
            temp = left 
            for i in range(left+1, right+1):
                temp = temp&i
        
            return right
        
        
        return 0
        
solution = Solution()

print(solution.rangeBitwiseAnd(left = 5, right = 7))
print(solution.rangeBitwiseAnd(left = 0, right = 0))
print(solution.rangeBitwiseAnd(left = 5, right = 7))
