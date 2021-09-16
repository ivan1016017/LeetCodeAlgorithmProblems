from typing import List 


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        first_word: str = words[0]
        for word in words[1:]:
            for letter in first_word:
                if letter in word:
                    word = word.replace(letter, "",1)
                else: 
                    first_word = first_word.replace(letter,"",1)

        return first_word

solution = Solution()


# print(solution.commonChars(words = ["bella","label","roller"]))

sample = "abcda"
new_sample = sample.replace("a","", 2)
print(new_sample)