import math
from typing import List


if __name__ == '__main__':
    class Solution:
        def threeSumClosest(self, nums: List[int], target: int) -> int:

            temp = math.inf
            result = None
            if len(nums) <3:
                return []
            else:
                for i in range(len(nums)):
                    for j in range(i+1,len(nums)):
                        for k in range(j+1,len(nums)):
                            if abs(nums[i] + nums [j] + nums[k] - target) < temp:
                                temp = abs(nums[i] + nums [j] + nums[k] - target)
                                result = nums[i] + nums [j] + nums[k]
                            if abs(nums[i] + nums [j] + nums[k] - target) == 0:
                                return target
            return result

    solution = Solution()
    print(solution.threeSumClosest([-1,2,1,-4], 1))
