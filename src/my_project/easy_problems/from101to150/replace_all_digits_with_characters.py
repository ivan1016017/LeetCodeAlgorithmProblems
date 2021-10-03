from typing import List 

class Solution:
    def replaceDigits(self, s: str) -> str:

        temp: str = ""
        answer: str = ""

        for character in range(1, len(s), 2):
            x = ord(s[character-1])
            temp = chr(x + int(s[character]))
            answer += s[character-1] + temp 

        if len(s)%2 ==1:
            answer += s[len(s)-1]


        return answer 


solution = Solution()

print(solution.replaceDigits(s = "a1c1e1"))

print(solution.replaceDigits( s = "a1b2c3d4e"))



