from typing import List 

class Solution:
    def minPartitions(self, n: str) -> int:
        
        answer = 0
        len_n: int = len(n)
        
        for i in range(len_n):
            if int(n[i]) > answer:
                answer = int(n[i])
                
        
        
        return answer
    
    
solution = Solution()


print(solution.minPartitions(n = "32"))

print(solution.minPartitions(n = "82734"))

print(solution.minPartitions( n = "27346209830709182346"))
