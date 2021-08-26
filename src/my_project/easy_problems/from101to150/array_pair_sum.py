from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:


        # initialize variables
        nums.sort()
        count: int = 0
        len_nums = len(nums)

        for i in range(0,len_nums,2):
            count += nums[i]



        return count


solution = Solution()
print(solution.arrayPairSum(nums = [6,2,6,5,1,2]))