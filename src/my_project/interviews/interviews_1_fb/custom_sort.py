from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def customSortString(self, order: str, s: str) -> str:

        answer = list()
        for o in order:
            answer.append(o*s.count(o))

        for c in s:
            if c not in order:
                answer.append(c)

        return ''.join(answer)

