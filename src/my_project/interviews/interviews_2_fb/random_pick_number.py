from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
import random 

class Solution:

    def __init__(self, nums: List[int]):
        self.map = {}
        for index, n in enumerate(nums):
            if n in self.map:
                self.map[n].append(index)
            else:
                self.map[n] = [index]

    def pick(self, target: int) -> int:
        indices = self.map[target]
        return random.choice(indices)


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

