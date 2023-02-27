from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        word_one = ''.join(word1)
        word_two = ''.join(word2)

        return word_one == word_two

        