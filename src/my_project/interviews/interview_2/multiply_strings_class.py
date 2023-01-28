from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        dict_solution = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

        temp1 = 0
        temp2 = 0

        len_num1 = len(num1)
        len_num2 = len(num2)

        for i in range(len_num1):
            temp1 += dict_solution[num1[i]]*(10**(len_num1-1-i))

        for i in range(len_num2):
            temp2 += dict_solution[num2[i]]*(10**(len_num2-1-i))

        return str(temp1*temp2)