from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # initialize variables
        len_nums = len(nums)
        first_greatest_num: int = 0
        second_greatest_num: int = 0

        for i in range(len_nums):

            if nums[i] > first_greatest_num:
                second_greatest_num = first_greatest_num
                first_greatest_num = nums[i]
            elif nums[i] > second_greatest_num:
                second_greatest_num = nums[i]
        return (first_greatest_num -1)*(second_greatest_num-1)


class SecondSolution:
    def maxProduct(self, nums: List[int]) -> int:

        # initialize variables
        len_nums = len(nums)
        count: int = 0
        max = -float('inf')

        for i in range(len_nums):
            for j in range(i+1, len_nums):
                if (nums[i]-1)*(nums[j]-1) > max:
                    print((nums[i]-1)*(nums[j]-1))
                    max = (nums[i]-1)*(nums[j]-1)
        return max

solution = Solution()
print(solution.maxProduct(nums = [3,4,5,2]))

print(-1234234 > -float('inf'))