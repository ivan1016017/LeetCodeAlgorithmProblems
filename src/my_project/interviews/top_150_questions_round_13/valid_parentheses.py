from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def isValid(self, s):

        dic_parentheses = {'(':')','[':']','{':'}'}
        check_lst = list()

        for p in s: 
            if p in dic_parentheses:
                check_lst.append(p)
            else:
                if len(check_lst) == 0 \
                                    or dic_parentheses[check_lst.pop()] != p:
                    return False 
        
        return len(check_lst) == 0