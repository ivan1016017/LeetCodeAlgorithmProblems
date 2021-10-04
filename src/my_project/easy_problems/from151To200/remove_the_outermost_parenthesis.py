from typing import List 

class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        left_count: int = 0
        right_count: int = 0
        count = 0
        answer = ""

        for character in s: 
            if character == "(":
                left_count += 1
            elif character == ")":
                right_count += 1
            
            count += 1
            if left_count == right_count:
                answer += s[(count - 2*left_count + 1): count-1]
                left_count = 0
                right_count = 0
                

            



        return answer

solution = Solution()

print(solution.removeOuterParentheses(s = "(()())(())"))

print(solution.removeOuterParentheses(s = "(()())(())(()(()))"))

print(solution.removeOuterParentheses(s = "()()"))



print("abcdef"[1:3])