from typing import List
from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counts = defaultdict(int)
        for i in range(len(nums)):
            counts[nums[i]] += 1
            if i > k:
                counts[nums[i - k - 1]] -= 1
            if counts[nums[i]] >1:
                return True
        return False



solution =Solution()
print(solution.containsNearbyDuplicate([1,2,3,4,1],3))