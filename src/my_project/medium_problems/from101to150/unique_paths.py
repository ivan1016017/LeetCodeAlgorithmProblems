from typing import List 

def fact(n):  
    return 1 if (n==1 or n==0) else n * fact(n - 1);  

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        numerator = fact(n+m-2)
        denominator = fact(n-1) * fact(m-1)
        return int(numerator/denominator)