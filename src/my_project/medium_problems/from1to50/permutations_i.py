from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(nums, index = 0):
            if index == len(nums):
                ans.append([] + nums)
                return
            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                print(ans)
                dfs(nums, index + 1)
                nums[i], nums[index] = nums[index], nums[i]
        dfs(nums, 0)
        return ans

solution = Solution()

print(solution.permute([1,2,3]))