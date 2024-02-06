from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def romanToInt(self, s: str) -> int:

        roman_to_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        len_s = len(s)
        answer = roman_to_dict[s[len_s-1]]

        for i in range(len_s-1):
            if roman_to_dict[s[len_s-2-i]] < roman_to_dict[s[len_s-1-i]]:
                answer -= roman_to_dict[s[len_s-2-i]] 
            else: 
                answer += roman_to_dict[s[len_s-2-i]] 

        return answer