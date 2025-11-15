from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1
        ls = nums[l]
        rs = nums[r]
        answer = 0

        while l < r:

            if ls == rs:
                l += 1
                r -= 1
                ls = nums[l]
                rs = nums[r]
            elif ls < rs:
                l += 1
                ls += nums[l]
                answer += 1
            else:
                r -= 1
                rs += nums[r]
                answer += 1

        return answer
