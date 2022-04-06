from typing import List 
import collections 

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ans = 0
        n = len(arr)
        level2 = collections.defaultdict(int)
        for i in range(2, n):
            for j in range(i-1):
                level2[arr[j] + arr[i-1]] += 1
            ans = ans + level2[target - arr[i]]
            ans = ans % (10**9 + 7)
        return ans