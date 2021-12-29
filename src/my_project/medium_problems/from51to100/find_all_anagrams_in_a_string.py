from typing import List 

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        
        # Create ASCII dictionary of 26 characters for p
        pCounter = [0] * 26
        for char in p:
            pCounter[ord(char) - ord('a')] += 1
        
        # Same thing for s, except leave the last char
        sCounter = [0] * 26
        for char in s[:len(p)-1]:
            sCounter[ord(char) - ord('a')] += 1
        
        # Loop through sliding window, keep adding and deleting characters as it goes
        for i in range(len(p) - 1, len(s)):

            # Introduce a new character
            sCounter[ord(s[i]) - ord('a')] += 1
            
            # Check if ASCII dictionary is same
            if sCounter == pCounter:
                ans.append(i-len(p)+1)
                
            # Remove old character
            sCounter[ord(s[i-len(p)+1]) - ord('a')] -= 1            

        return ans
        