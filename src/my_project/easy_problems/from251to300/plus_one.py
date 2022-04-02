from typing import List
from unicodedata import digit 

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits)-1,-1,-1):
            if digits[i] != 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
                
        if digits[0] == 0:
            digits = [1] + digits 
        
        return digits


class SecondSolution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        temp = 0
        temp_list = list()
        len_digits = len(digits)
        for i in range(len_digits):
            temp += digits[len_digits - 1 - i]*(10**i)
        temp += 1
        
        
        if temp // (10**len_digits) == 0:
            for i in range(len_digits):
                temp_list.append(temp // (10**(len_digits -1 - i)))
                temp -= (10**(len_digits -1 - i))*temp_list[-1]
            return temp_list
        else: 
            for i in range(len_digits+1):
                temp_list.append(temp // (10**(len_digits + 1 - 1 - i)))
                temp -= (10**(len_digits + 1 - 1 - i))*temp_list[-1]
            return temp_list