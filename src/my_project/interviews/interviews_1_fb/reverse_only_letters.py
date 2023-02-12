from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = ['a','e','i','o','u','A','E','I','O','U']
        temp = list()
        ids = list()
        for k,v in enumerate(s):
            if v in vowels:
                temp.append(v)
                ids.append(k)

        temp.reverse()

        s = [x for x in s]

        for i in range(len(ids)):
            s[ids[i]] = temp[i]

        return ''.join(s)

