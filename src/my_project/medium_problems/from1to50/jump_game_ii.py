from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:

        target = len(nums) - 1
        count = 0

        while target > 0:
            idx = 0

            while nums[idx] + idx < target:
                idx += 1

            target = idx

            count += 1

        return count


solution = Solution()

print(solution.jump([1,1,1,1,1,1,1,10,1,1]))