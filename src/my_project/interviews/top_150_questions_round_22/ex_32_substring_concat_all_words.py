from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
import collections

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words: return []
        LS, M, N, C = len(s), len(words), len(words[0]), collections.Counter(words)
        return [i for i in range(LS-M*N+1) if collections.Counter([s[a:a+N] for a in range(i,i+M*N,N)]) == C]