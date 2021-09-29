from typing import List 

class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        s = sorted(s, key=lambda x: int(x[-1]))
        return ' '.join(x[:-1] for x in s)


solution = Solution()

print(solution.sortSentence(s = "is2 sentence4 This1 a3"))