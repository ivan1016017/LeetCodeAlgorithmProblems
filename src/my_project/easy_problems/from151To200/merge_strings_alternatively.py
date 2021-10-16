from typing import List 

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        answer: str = ''
        min_length = min(len(word1), len(word2))
        for i in range(min_length):
            answer += word1[i] + word2[i]

        if len(word1) < len(word2):
            answer += word2[min_length:]
            return answer 
        if len(word1) > len(word2):
            answer += word1[min_length:]
            return answer 

        return answer 

solution = Solution()

print(solution.mergeAlternately(word1 = "abc", word2 = "pqr"))

print(solution.mergeAlternately(word1 = "ab", word2 = "pqrs"))

print(solution.mergeAlternately(word1 = "abcd", word2 = "pq"))
