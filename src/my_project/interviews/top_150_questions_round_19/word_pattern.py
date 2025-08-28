from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        dic_answer = dict()

        words = s.split(' ')

        if len(words) != len(pattern) or len(set(words)) != len(set(pattern)):
            return False 
        else:
            for k, v in enumerate(words):
                if v in dic_answer:
                    if dic_answer[v] != pattern[k]:
                        return False 
                else:
                    dic_answer[v] = pattern[k]

            return True 