from typing import List 

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s = s.strip()
        
        temp = 0
        for i in range(len(s)):
            if s[i] == " ":
                temp = 0
                continue
            temp += 1

        return temp
        
        
        
solution = Solution()

print(solution.lengthOfLastWord("   fly me   to   the moon       "))