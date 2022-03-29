from typing import List 

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        temp_dict = dict()
        
        for num in nums:
            temp_dict[num] = 0
            
        for num in nums:
            temp_dict[num] += 1
            
        answer = True
        
        for key, value in temp_dict.items():
            if value % 2 != 0:
                answer = not answer 
                return answer
        
        
        return answer
    
solution = Solution()

print(solution.divideArray([3,2,3,2,2,2]))