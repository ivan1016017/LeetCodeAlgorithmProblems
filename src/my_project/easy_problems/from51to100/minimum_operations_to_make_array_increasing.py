from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:

        # initialize variables
        count = 0
        len_nums = len(nums)

        for i in range(1, len_nums):
            if nums[i-1] >= nums[i]:
                count += nums[i-1] - nums[i] + 1
                nums[i] = nums[i-1] + 1


        return count

solution = Solution()

print(solution.minOperations(nums = [1,5,2,4,1]))