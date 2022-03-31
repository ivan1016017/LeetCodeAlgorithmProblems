from typing import List 

class Solution:
    def isValid(self, s: str) -> bool:
        temp_list = list()
        current = None 
        list_parentheses = ["(","[","{"]
        
        for parenteses in s:
            if parenteses in list_parentheses:
                temp_list.append(parenteses)
            else: 
                if not temp_list:
                    return False 
                current = temp_list.pop()
                if current == "(":
                    if parenteses != ")":
                        return False 
                elif current == "[":
                    if parenteses != "]":
                        return False 
                elif current == "{":
                    if parenteses != "}":
                        return False 
                    
        if temp_list: 
            return False 
        return True 