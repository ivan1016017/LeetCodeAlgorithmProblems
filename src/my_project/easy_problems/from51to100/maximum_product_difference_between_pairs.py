from typing import List

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:


        len_nums = len(nums)
        nums = sorted(nums)

        solution = nums[len_nums-1]*nums[len_nums-2] - nums[0]*nums[1]


        return solution

class SecondSolution:
    def maxProductDifference(self, nums: List[int]) -> int:

        temp_max = float('-inf')
        temp_min = float('inf')
        len_nums = len(nums)

        for i in range(len_nums):
            for j in range(i+1, len_nums):
                if nums[i]*nums[j] > temp_max:
                    temp_max = nums[i]*nums[j]
                if nums[i]*nums[j] < temp_min:
                    temp_min = nums[i]*nums[j]

        return temp_max - temp_min


solution = Solution()
print(solution.maxProductDifference(nums = [4,2,5,9,7,4,8]))




