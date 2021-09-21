from typing import List 
from collections import Counter


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        c = Counter(nums)

        cc = sorted(nums, key=lambda l: (c[l],-l))



        return cc

solution = Solution()

print(solution.frequencySort(nums = [1,1,2,2,2,3]))
