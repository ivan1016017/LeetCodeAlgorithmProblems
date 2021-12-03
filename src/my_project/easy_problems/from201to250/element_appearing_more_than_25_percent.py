from typing import List 

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        # initialize variables    
        len_arr: int = len(arr)
        temp_dict = dict()
        answer: int  = -1
        
        for i in range(len_arr):
            temp_dict[arr[i]] = 0
            
        for i in range(len_arr):
            temp_dict[arr[i]] += 1/len_arr
            
        for i in range(len_arr):
            if temp_dict[arr[i]] > 0.25:
                answer = arr[i]
                return answer 
        
        return answer 
    
    
solution = Solution()

print(solution.findSpecialInteger(arr = [1,2,2,6,6,6,6,7,10]))

print(solution.findSpecialInteger(arr = [1,1]))
