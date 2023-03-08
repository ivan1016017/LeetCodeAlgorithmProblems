from typing import List, Union, Collection,  Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def checkRecord(self, s: str) -> bool:

        criterion_one = True
        criterion_two = True 

        count_l = 0
        count_a = 0

        for c in s: 
            if c == 'L':
                count_l += 1
            else:
                count_l = 0

            if count_l == 3:
                criterion_two = False 
            
            if c == 'A':
                count_a += 1
            
            if count_a >=2: 
                criterion_one = False 

            if not criterion_one and not criterion_two:
                return  criterion_one and criterion_two
            
        return criterion_one and criterion_two
            
        

