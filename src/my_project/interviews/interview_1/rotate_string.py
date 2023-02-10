from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        answer = list()
        answer.append(s)
        num_rotations = len(s)-1

        while num_rotations > 0:
            s = s[1:] + s[0]
            answer.append(s)
            num_rotations -= 1

        return goal in answer

a = 'abbc'

print(a.index('b'))