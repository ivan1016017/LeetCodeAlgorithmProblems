from typing import List 

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        left, right = 0, num 
        
        while left <= right:
            
            mid = (left+right)//2
            
            if mid**2 == num: 
                return True
            elif mid**2 > num:
                right = mid-1
            else:
                left = mid+1
        
        return False 