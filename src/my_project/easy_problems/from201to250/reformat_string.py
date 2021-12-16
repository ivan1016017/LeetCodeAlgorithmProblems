from typing import List, overload 

class Solution:
    def reformat(self, s: str) -> str:
        
        def is_alpha(x):
            is_uppercase = ord(x) >= 65 and ord(x) <= 90
            is_lowercase = ord(x) >=97 and ord(x) <= 122
            return is_uppercase or is_lowercase
        def is_numeric(x):
            is_numeric = ord(x)>= 48 and ord(x) <= 57
            return is_numeric
        
        s1 = ''.join([x for x in s if is_alpha(x)])
        s2 = ''.join([x for x in s if is_numeric(x)])
        print(s1)
        print
        if abs(len(s1) - len(s2))> 1: 
            return ''
        
        
        if len(s1) < len(s2):
            s1, s2 = s2, s1
            
        answer = ''
        for i in range(len(s2)):
            answer += s1[i] + s2[i]
            
        if len(s1)> len(s2):
            answer += s1[-1]
        

        
        return answer 
    
solution = Solution()

print(solution.reformat(s = "a0b1c2"))