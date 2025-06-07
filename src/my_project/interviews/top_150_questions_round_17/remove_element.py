from typing import List, Union, Collection, Mapping, Optional
from abc import ABC

class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:

        while val in nums:

            nums.remove(val)

        return len(nums)

