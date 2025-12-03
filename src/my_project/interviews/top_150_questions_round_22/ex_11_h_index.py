from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations.sort(reverse=True)
        len_cit:int = len(citations)
        answer:int = 0

        for i in range(len_cit):

            if citations[i] >= i + 1:
                answer = i + 1

        return answer
