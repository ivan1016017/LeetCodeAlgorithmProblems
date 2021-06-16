from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp = list()
        for i in range(len(nums)):
            temp.append(sum(nums[0:i+1]))
        return temp


solution = Solution()

print(solution.runningSum([1,2,3,4]))

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
