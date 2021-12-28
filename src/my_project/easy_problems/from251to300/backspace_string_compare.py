from typing import List

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        # Helper to process a string
        def process(str):
          newS = ""
          for i in str:
            # Backspace to drop last character
            if i == "#":
              newS = newS[:-1]
            # Normal character so add it
            else:
              newS += i
          return newS
        
        # Run the helper for both strings and compare
        if process(s) == process(t) : 
          return True
        return False
    
solution = Solution()

print(solution.backspaceCompare(s = "ab#c", t = "ad#c"))

print(solution.backspaceCompare(s = "ab##", t = "c#d#"))

print(solution.backspaceCompare(s = "a#c", t = "b"))

sample = 'abcd'
print(sample[:-1])
