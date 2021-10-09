from typing import List 

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count: int = 0
        for letter in patterns:
            if letter in word:
                count += 1

        return count 


solution = Solution()

print(solution.numOfStrings(patterns = ["a","abc","bc","d"], word = "abc"))

print(solution.numOfStrings(patterns = ["a","b","c"], word = "aaaaabbbbb"))

print(solution.numOfStrings(patterns = ["a","a","a"], word = "ab"))
