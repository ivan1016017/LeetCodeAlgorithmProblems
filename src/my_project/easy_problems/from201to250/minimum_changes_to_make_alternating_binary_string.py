from typing import List 


class Solution:
    def minOperations(self, s: str) -> int:
        
        first_dict = {}
        second_dict = {}
        len_s: int = len(s)
        min_count_first_dict: int = 0
        min_count_second_dict: int = 0
        
        for i in range(len_s):
            first_dict[i] = str((i+1)%2)
            
            
        for i in range(len_s):
            if s[i] == first_dict[i]:
                min_count_first_dict += 1
            else: 
                min_count_second_dict += 1
                
        answer = min(min_count_first_dict, min_count_second_dict)
                
            
        
        
        return answer 
    
    
solution = Solution()


print(solution.minOperations( s = "0100"))

print(solution.minOperations(s = "10"))

print(solution.minOperations(s = "1111"))

print(solution.minOperations("10010100"))

