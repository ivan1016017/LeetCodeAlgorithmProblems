from typing import List 

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        answer: List[int] = list()
        len_nums: int = len(nums)
        
        temp_dict = dict()
        
        for i in range(1,len_nums+1):
            temp_dict[i] = 0
            
        for i in range(len_nums):
            temp_dict[nums[i]] += 1
            
        for num in temp_dict.keys():
  
            if temp_dict[num] == 0:
                answer.append(num)
        
        
        return answer
    
    
solution = Solution()

print(solution.findDisappearedNumbers(nums = [4,3,2,7,8,2,3,1]))

print(solution.findDisappearedNumbers(nums = [1,1]))
