from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def reverseWords(self, s: str) -> str:

        lst_words = s.split()
        lst_words.reverse()
        return ' '.join(lst_words)