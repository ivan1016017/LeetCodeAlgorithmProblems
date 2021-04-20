from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))



solution = Solution()

print(solution.containsDuplicate([1,2,3,4]))

