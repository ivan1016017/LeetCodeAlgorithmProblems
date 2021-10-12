from typing import List 

class Solution:
    def generateTheString(self, n: int) -> str:
        first_letter: str = "a"
        second_letter: str = 'b'
        answer: str = ''
        if n%2 == 0:
            answer = first_letter*(n-1) + second_letter
        else:
            answer = first_letter*n 
        return answer 


solution = Solution()

print(solution.generateTheString(n= 4))

print(solution.generateTheString(n=2))

print(solution.generateTheString(n=7))
