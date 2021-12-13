from typing import List 

class Solution:
    def thousandSeparator(self, n: int) -> str:
        
        x=str(n)[::-1]
        
        chunks, chunk_size = len(x), 3
        l = [ x[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
        
        return ('.'.join(l))[::-1]
        
        
        
        
        
    
    
solution = Solution()

print(solution.thousandSeparator(12345))