from typing import List 


class Solution:
    def countBits(self, n: int) -> List[int]:
        
        answer = []
        
        for i in range(n+1):
            answer.append(self.countOnes(i))
            
        
        return answer
        
        
    
    def countOnes(self, n: int) -> int:
        count = 0
        quotient = n
        while quotient > 0:
            remainder = n % 2
            quotient = n // 2
            n = quotient
            
            if remainder == 1:
                count += 1
        
        
        return count
    
    
class SolutionTwo:
    def countBits(self, n: int) -> List[int]:
        

        if n == 0: return [0]
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            if i%2 == 0: dp[i] = dp[i//2]
            else: dp[i] = 1 + dp[(i-1)//2]
                
        return dp


