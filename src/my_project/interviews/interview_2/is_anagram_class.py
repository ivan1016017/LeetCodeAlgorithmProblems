from typing import List, Union, Mapping, Collection, Optional
from abc import ABC, abstractmethod

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_list = [l for l in s]
        t_list = [l for l in t]
        s_list.sort()
        t_list.sort()


        return s_list == t_list 

solution = Solution()

print(solution.isAnagram(s = "anagram", t = "nagaram"))