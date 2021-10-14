from typing import List 

class Solution:
    def reverseWords(self, s: str) -> str:

        temp_list = list()
        answer = ""
        temp_word = ""
        for word in s.split():
            temp_word = ""
            for letter in word:
                temp_word = letter + temp_word

            temp_list.append(temp_word)

        return " ".join(temp_list)



solution = Solution()
print(solution.reverseWords(s = "Let's take LeetCode contest"))