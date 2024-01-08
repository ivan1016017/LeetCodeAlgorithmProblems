from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
import re 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # transform to lowercase 
        s = s.lower()

        # remove non-alphanumeric characters
        temp = re.sub(pattern='[^a-zA-Z0-9]', repl='',string=s)
        len_temp = len(temp) 

        # check if temp is palindrome
        for i in range(len_temp//2):
            if temp[i] != temp[len_temp-1-i]:
                return False 
        return True
        
