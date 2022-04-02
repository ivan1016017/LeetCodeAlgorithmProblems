from typing import List 

class Solution:
    def mySqrt(self, x: int) -> int:
        
        left, right = 0, x 
        
        while left <= right:
            
            mid = (left + right) // 2
            
            if mid**2 > x:
                right = mid - 1
            elif mid**2 < x:
                left = mid + 1 
            else:
                return mid 
            
        return right
            