from typing import List 

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        answer: int = -1
        len_nums: int = len(nums)
        
        for i in range(len_nums):
            for j in range(i+1, len_nums):
                temp = nums[j] - nums[i]
                if temp > 0 and temp > answer:
                    answer = temp
        
        
        return answer 
    
solution = Solution()

print(solution.maximumDifference(nums = [7,1,5,4]))

print(solution.maximumDifference(nums = [9,4,3,2]))

print(solution.maximumDifference(nums = [1,5,2,10]))
