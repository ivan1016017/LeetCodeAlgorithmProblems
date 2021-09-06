from typing import List

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:

        nums.sort(reverse=True)
        left_sum: int = 0
        right_sum: int = 0




        for i in range(len(nums)+1):
            left_sum = sum(nums[:i])
            right_sum = sum(nums[i:])
            if left_sum > right_sum:
                return nums[:i]



        return nums[:i]



solution = Solution()

print(solution.minSubsequence(nums = [4,3,10,9,8]))

print(solution.minSubsequence(nums = [4,4,7,6,7]))

print(solution.minSubsequence(nums = [4,4]))

print(solution.minSubsequence(nums = [4]))