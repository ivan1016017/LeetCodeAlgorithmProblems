from typing import List 

class Solution:
    def countPoints(self, rings: str) -> int:
        
        dict_answer = {}
        
        numbers = '0123456789'
        
        for i in range(10):
            dict_answer[numbers[i]] = []
            
        for i in range(0,len(rings),2):
            
            if rings[i] not in dict_answer[rings[i+1]]:
                dict_answer[rings[i+1]].append(rings[i]) 
            
        answer: int = 0
        
        for i in range(10):
            if len(dict_answer[numbers[i]]) == 3:
                answer += 1
                
        
        
        
        return answer 
    
solution = Solution()

print(solution.countPoints(rings = "B0B6G0R6R0R6G9"))


# function to be reverted
def function_to_be_reverted(nums):
    return nums