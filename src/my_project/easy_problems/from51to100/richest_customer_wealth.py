from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        len_accounts = len(accounts)

        for i in range(len_accounts):
            accounts[i] = self.computeSum(accounts[i])

        return self.computeMax(accounts)

    def computeMax(self, nums: List[int]):
        # initialize variables
        max_index = 0
        temp_max = nums[max_index]
        len_nums = len(nums)
        # compute max
        for i in range(1, len_nums):

            if nums[max_index] < nums[i]:
                temp_max = nums[i]
                max_index = i
        return temp_max

    def computeSum(self, nums: List[int]):
        # initialize variables
        temp = 0
        len_nums = len(nums)
        # compute sum
        for i in range(len_nums):
            temp += nums[i]
        return temp


solution = Solution()
print(solution.computeMax([1, 2, 134, 3, 939]))
print(solution.computeSum([1, 2, 3, 4, 5]))



print(solution.maximumWealth([[1,5],[7,3],[3,5]]))