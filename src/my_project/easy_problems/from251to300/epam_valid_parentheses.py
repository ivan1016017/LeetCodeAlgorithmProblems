from typing import List 

class Solution:
    def isValid(self, s: str) -> bool:
        
        temp = list()        
        list_parentheses = ["(","[","{"]
        
        for p in s:
            if p in list_parentheses:
                temp.append(p)
            else:
                if not temp:
                    return False
                other_half = temp.pop()
                
                if p == ")":
                    if other_half != "(":
                        return False 
                elif p == "]":
                    if other_half != "[":
                        return False 
                elif p == "}":
                    if other_half != "{":
                        return False 
                else: 
                    return False
                
        if temp:
            return False

        
        return True