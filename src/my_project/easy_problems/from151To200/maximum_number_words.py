from typing import List 

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        count: int = 0
        list_words: List[str] = text.split(' ')

        for word in list_words:
            for letter in brokenLetters:
                if letter in word:
                    count += 1
                    break
            

        return len(list_words) - count

solution = Solution()

print(solution.canBeTypedWords(text = "hello world", brokenLetters = "ad"))

print(solution.canBeTypedWords(text = "leet code", brokenLetters = "lt"))

print(solution.canBeTypedWords(text = "leet code", brokenLetters = "e"))
