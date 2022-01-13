from typing import List 
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.arr = nums.copy()
        
    def reset(self) -> List[int]:
        self.nums[:] = self.arr
        return self.nums

    def shuffle(self) -> List[int]:
        # shuffle returns none, so copy and shuffle 
        
        # approach 1 
        ans = self.arr[:]
        random.shuffle(ans)
        return ans