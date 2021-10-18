from typing import List 

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:


        def fromStringToCode(word: str) -> int:
            temp = 0
            len_word = len(word)
            for i in range(len(word)-1,-1,-1):
                # print((ord(word[i])%97)* (10**(i)), word[i])
                temp += (ord(word[i])%97)* (10**(len_word -1- i))


            return temp

        
        
        return fromStringToCode(firstWord) + fromStringToCode(secondWord) == fromStringToCode(targetWord) 

solution = Solution()

print(solution.isSumEqual(firstWord = "acb", secondWord = "cba", targetWord = "cdb"))

print(solution.isSumEqual(firstWord = "aaa", secondWord = "a", targetWord = "aab"))

print(solution.isSumEqual(firstWord = "aaa", secondWord = "a", targetWord = "aaaa"))

sample = 'abc'

for i in range(len(sample)):
    print(sample[i])
