from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        temp = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[temp] = nums[i]
                temp += 1

        return temp




solution = Solution()
print(solution.removeElement([2,2,3,5,6],2))