from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        temp = [word for word in s]
        shift_temp = ["" for _ in range(len(s))]

        for i in range(len(s)):
            shift_temp[indices[i]] = temp[i]
        
        return ''.join(shift_temp)
    
solution = Solution()

print(solution.restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))