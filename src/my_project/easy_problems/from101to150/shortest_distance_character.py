from typing import List 

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:

        index_target: List[int] = list()
        solution: List[int] = list()
        temp = None

        for i in range(len(s)):
            if s[i] == c:
                index_target.append(i)
             
        for i in range(len(s)):
            temp = min([abs(x - i) for x in index_target])            
            solution.append(temp)

        return solution

solution = Solution()

print(solution.shortestToChar(s = "loveleetcode", c = "e"))