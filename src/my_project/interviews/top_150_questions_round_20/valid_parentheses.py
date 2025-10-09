from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def isValid(self, s):

        dic_parentheses = {'(':')','[':']','{':'}'}

        check_list = list()

        for p in s:

            if p in dic_parentheses:
                check_list.append(p)
            else: 
                if len(check_list) == 0 or \
                        dic_parentheses[check_list.pop()] != p:
                    return False 
                
        return len(check_list) == 0