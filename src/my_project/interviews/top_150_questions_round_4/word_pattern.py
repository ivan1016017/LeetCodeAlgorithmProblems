from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import defaultdict

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        dic_answer = defaultdict(str) 
        words = s.split(' ')

        if len(words) != len(pattern) or len(set(words)) != len(set(pattern)):
            return False 
        else: 
            for k, v in enumerate(pattern):
                if v in dic_answer:
                    if dic_answer[v] != words[k]:
                        return False 
                else: 
                    dic_answer[v] = words[k]

            return True 
