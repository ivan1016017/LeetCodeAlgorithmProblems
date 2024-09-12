from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution(object):
    def isHappy(self, n):

        set_answer = set()

        while n != 1:

            if n in set_answer:
                return False 
            else:
                set_answer.add(n)
                
            n = sum([int(c)**2 for c in str(n)])
            
        return True 