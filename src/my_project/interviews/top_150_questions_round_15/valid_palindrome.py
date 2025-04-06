from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
import re 

class Solution:
    def isPalindrome(self, s: str) -> bool:

        # to lower case
        s = s.lower()

        # remove non-alphanumeric characters
        s = re.sub(pattern='[^a-zA-Z0-9]', repl='', string=s)

        len_s = len(s)

        for i in range(len_s//2):

            if s[i] != s[len_s - 1 -i]:
                return False 
            
        return True
