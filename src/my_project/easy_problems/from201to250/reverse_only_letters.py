from typing import List 

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        n = len(s)

        temp = {i:s[i]  for i in range(len(s)) if not s[i].isalpha()}

        
        s = [s[i] for i in range(len(s)) if s[i].isalpha()]


        s = list(reversed(s))

        for i in range(0,n):
            if i in temp:
                s.insert(i,temp[i])
                
        return ("".join(s))
    
    
solution = Solution()

print(solution.reverseOnlyLetters(s = "ab-cd"))

print(solution.reverseOnlyLetters(s = "a-bC-dEf-ghIj"))

print(solution.reverseOnlyLetters(s = "Test1ng-Leet=code-Q!"))
