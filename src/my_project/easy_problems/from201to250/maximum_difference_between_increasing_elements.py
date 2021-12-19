from typing import List 
import math
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        answer: int = -1
        min_val =  math.inf
        len_nums: int = len(nums)
        
        for i in range(len_nums):
            if nums[i] < min_val:
                min_val = nums[i]
            elif nums[i] - min_val > 0:
                answer = max(answer, nums[i] - min_val)
        
        
        return answer 
    
solution = Solution()

print(solution.maximumDifference(nums = [7,1,5,4]))

print(solution.maximumDifference(nums = [9,4,3,2]))

print(solution.maximumDifference(nums = [1,5,2,10]))
