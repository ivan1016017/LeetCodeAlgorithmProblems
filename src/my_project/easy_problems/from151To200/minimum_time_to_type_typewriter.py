from typing import List 

class Solution:
    def minTimeToType(self, word: str) -> int:

        answer = 0
        prev = 'a'
        for letter in word:
            if abs(ord(letter) - ord(prev))> 13:
                answer += 26 - abs(ord(letter) - ord(prev))
            else: 
                answer += abs(ord(letter) - ord(prev))

            prev = letter 
            answer += 1


        return answer 


solution = Solution()

print(solution.minTimeToType(word = "abc"))

print(solution.minTimeToType(word = "bza"))

print(solution.minTimeToType(word = "zjpc"))
