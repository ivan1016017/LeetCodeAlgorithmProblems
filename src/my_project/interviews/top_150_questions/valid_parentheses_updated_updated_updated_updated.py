from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def isValid(self, s):
        d = {'(':')', '{':'}','[':']'}
        check_lst = list()
        for i in s: 
            if i in d: 
                check_lst.append(i)
            elif len(check_lst) == 0 or d[check_lst.pop()] != i:
                return False 
        return len(check_lst) == 0