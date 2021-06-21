from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        len_nums = len(nums)

        if len_nums < 3:
            return 0

        temp_list = [0 for x in range(len_nums)]
        result = 0

        for i in range(2,len_nums):
            if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                temp_list[i] = 1

        for j in range(2, len_nums):
            if nums[j] -nums[j-1] == nums[j-1] - nums[j-2]:

                temp_list[j] =  temp_list[j-1] + temp_list[j]
                print(temp_list)

        for i in range(2,len_nums):
            result += temp_list[i]


        return result

solution = Solution()

print(solution.numberOfArithmeticSlices([1,2,3,4]))

print(solution.numberOfArithmeticSlices([1,2,3,4,5]))
