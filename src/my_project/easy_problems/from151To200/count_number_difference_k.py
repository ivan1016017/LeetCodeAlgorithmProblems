from typing import List 

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count: int = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if abs(nums[i]-nums[j]) == k:
                    count += 1

        return count 


solution = Solution()

print(solution.countKDifference(nums = [1,2,2,1], k = 1))

print(solution.countKDifference(nums = [1,3], k = 3))

print(solution.countKDifference(nums = [3,2,1,5,4], k = 2))


