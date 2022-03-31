from typing import List 

class Solution:
    def romanToInt(self, s: str) -> int:
        
        len_s = len(s)
        
        if len_s >=1 and len_s <= 15:  
        
            # create the distionary
            roman_dict = {"I":1, "V":5, "X":10, "L":50,"C":100,"D":500,"M":1000}
            
            
            
            temp = roman_dict[s[len_s-1]]
            
            for i in range(len_s-1):
                
                if roman_dict[s[len_s -2 -i]] < roman_dict[s[len_s - 1 - i]]:
                    temp -= roman_dict[s[len_s -2  -i]]
                else: 
                    temp += roman_dict[s[len_s -2  -i]]
                    
            return temp

        else:
             return 0