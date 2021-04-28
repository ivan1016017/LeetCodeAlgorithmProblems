from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """

        temp = list()
        for i in nums:
            if i != 0:
                temp.append(i)
        len_temp = len(temp)
        for i in range(0, len(nums)- len_temp):
            temp.append(0)

        nums = temp
        print(nums)

solution = Solution()
solution.moveZeroes([0,1,0,3,12])