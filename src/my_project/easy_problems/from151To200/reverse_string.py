from typing import List 

class Solution:
    def reverseString(self, s: List[str]) -> None:
        len_s: int = len(s)
        for i in range(len_s//2):
            s[i], s[len_s-1-i] =  s[len_s-1-i] , s[i]
        return s 


solution = Solution()

print(solution.reverseString(s = ["h","e","l","l","o"]))

print(solution.reverseString(s = ["H","a","n","n","a","h"]))
