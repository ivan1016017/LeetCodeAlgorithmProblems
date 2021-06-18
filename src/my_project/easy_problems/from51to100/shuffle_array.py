from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        temp = list()

        for i in range(n):
            temp.append(nums[i])
            temp.append(nums[n+i])
        return temp

solution  = Solution()
print(solution.shuffle([2,5,1,3,4,7], 3))