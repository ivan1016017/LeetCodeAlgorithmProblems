from typing import List 

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        a = []
        for i, n in enumerate(nums):
            if n == key:
                a.append(i)
        
        res = []
        for i in range(len(nums)):
            isk = False
            for j in a:
                if abs(i-j) <= k:
                    isk = True
                    break
                    
            if isk:
                res.append(i)
        
        return res
        
        