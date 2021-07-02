from typing import List

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:

        count:int = 0
        temp: int = 0

        for item in s:
            if item == " ":
                count += 1
            if count == k:
                return s[0:temp]

            temp += 1
        return s


solution = Solution()
print(solution.truncateSentence(s = "Hello how are you Contestant", k = 4))