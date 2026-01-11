from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        answer = defaultdict(list)

        for word in strs:
            answer[''.join(sorted(word))].append(word)

        return list(answer.values())
