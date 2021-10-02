from typing import List 

class Solution:
    def toLowerCase(self, s: str) -> str:
        answer: str = ""
        x = ""
        for letter in s:
            if ord(letter) <= 90 and ord(letter) >= 65:
                x = chr(ord(letter) + 32)
                answer += x
            else:
                answer += letter


        return answer 


solution = Solution()

print(solution.toLowerCase(s = "Hello"))

print(solution.toLowerCase(s = "here"))


print(solution.toLowerCase(s = "LOVELY"))
