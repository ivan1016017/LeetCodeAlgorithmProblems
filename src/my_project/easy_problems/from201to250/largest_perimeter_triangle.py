from typing import List 

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort(reverse=True)
        len_nums: int = len(nums)
        answer: int = 0
        
        for i in range(2,len_nums):
            if nums[i-2] - nums[i-1] <nums[i]:
                answer = nums[i] + nums[i-1] + nums[i-2]
                return answer 
            
        
        return answer 
    
    
solution = Solution()

print(solution.largestPerimeter(nums = [2,1,2]))

print(solution.largestPerimeter(nums = [1,2,1]))

print(solution.largestPerimeter(nums = [3,2,3,4]))

print(solution.largestPerimeter(nums = [3,6,2,3]))
