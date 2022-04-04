from typing import List 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        x = str(x)
        len_x = len(x)
        for i in range(len_x//2):
            if x[i] != x[len_x - 1 -i]:
                return False 
        
        
        return True