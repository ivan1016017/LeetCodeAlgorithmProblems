from typing import List 

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        prev_count = 0
        current_count = 0
        answer = 0
        prev = -1
        
        for digit in s:
            
            if digit == prev:
                current_count += 1
            else: 
                answer += min(prev_count, current_count)
                prev_count, current_count = current_count, 1
            prev = digit 
            
            
        answer += min(prev_count, current_count)

        
        return answer 
    
    
solution = Solution()

print(solution.countBinarySubstrings(s = "00110011"))

print(solution.countBinarySubstrings(s = "10101"))


