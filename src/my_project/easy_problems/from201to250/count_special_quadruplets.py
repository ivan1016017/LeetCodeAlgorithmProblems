from typing import List 

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        answer: int = 0
        len_nums: int = len(nums)
        for i in range(len_nums):
            for j in range(i+1, len_nums):
                for k in range(j+1, len_nums):
                    for l in range(k+1, len_nums):
                        if nums[i] + nums[j] + nums[k] == nums[l]:
                            answer += 1
        
        return answer 
    
    
solution = Solution()

print(solution.countQuadruplets(nums = [1,2,3,6]))

print(solution.countQuadruplets(nums = [3,3,6,4,5]))

print(solution.countQuadruplets(nums = [1,1,1,3,5]))