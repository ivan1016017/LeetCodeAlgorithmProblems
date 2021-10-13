from typing import List 

class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        count: int = 0
        temp_negative: int = 0
        for num in nums: 
            count += num
            temp_negative = min(count, temp_negative)
            # if count < temp_negative:
            #     temp_negative = count 

        return abs(temp_negative) + 1

solution = Solution()

print(solution.minStartValue(nums = [-3,2,-3,4,2]))

print(solution.minStartValue(nums = [1,2]))

print(solution.minStartValue(nums = [1,-2,-3]))
