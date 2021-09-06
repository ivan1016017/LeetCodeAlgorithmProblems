from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # Inititalize variables
        len_nums = len(nums)

        if len_nums == 1:
            return True

        flag = 0
        solution = True

        for i in range(1,len_nums):

            if nums[i] - nums[i-1] > 0:
                flag = 1
                break
            elif nums[i] - nums[i-1] < 0:
                flag = -1
                break

        if flag == 0:
            return solution

        if flag == 1:
            for i in range(1,len_nums):
                if nums[i] - nums[i-1] < 0:
                    return False
            return solution

        if flag == -1:
            for i in range(1, len_nums):
                if nums[i] - nums[i-1] > 0:
                    return False
            return solution

solution = Solution()
print(solution.isMonotonic(nums = [1,1,1]))







