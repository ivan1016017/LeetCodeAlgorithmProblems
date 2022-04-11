from typing import List 

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n < 1:
            return False 
        
        elif n == 1:
            return True 
        
        
        temp = 1
        
        while temp < n:
            
            temp = temp*3
            
            if temp == n:
                return True 
            
        return False 
    
    
class SecondSolution:
    def isPowerOfThree(self, n: int) -> bool:
        
        return n > 0 == 3**19 % n