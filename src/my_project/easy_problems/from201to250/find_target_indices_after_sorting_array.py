from typing import List 

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        nums.sort()

        len_nums: int = len(nums)
        answer: List[int] = list()
        
        for i in range(len_nums):
            if nums[i] == target:
                answer.append(i)
                        
        
        return answer 
    
    
solution = Solution()

print(solution.targetIndices(nums = [1,2,5,2,3], target = 2))

print(solution.targetIndices(nums = [1,2,5,2,3], target = 3))

print(solution.targetIndices(nums = [1,2,5,2,3], target = 5))

print(solution.targetIndices( nums = [1,2,5,2,3], target = 4))
