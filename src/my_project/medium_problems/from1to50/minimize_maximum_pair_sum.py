from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:

        # initialize variables
        nums.sort()
        len_nums = len(nums)
        pair_sum= list()

        for i in range(len_nums//2):
            pair_sum.append(nums[i] + nums[len_nums - 1 -i])

        return max(pair_sum)

solution = Solution()
print(solution.minPairSum(nums = [3,5,2,3]))