from typing import List 

class Solution:
    def maxDepth(self, s: str) -> int:
        
        count:int  = 0
        answer: int = 0
        for character in s: 
            if character == "(":
                count += 1
            elif character == ")": 
                count -= 1
            
            if count > answer: 
                answer = count 




        return answer 

solution = Solution()

print(solution.maxDepth(s = "(1+(2*3)+((8)/4))+1"))

print(solution.maxDepth( s = "(1)+((2))+(((3)))"))


print(solution.maxDepth(s = "1+(2*3)/(2-1)"))


print(solution.maxDepth( s = "1"))
