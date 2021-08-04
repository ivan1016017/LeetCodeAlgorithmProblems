from typing import List

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        # initialize variables
        solution: list[str] = list()
        pattern: str = self.toCommonString(pattern)

        for word in words:
            if self.toCommonString(word) == pattern:
                solution.append(word)


        return solution




    def toCommonString(self, word: str) -> str:


        temp_list: List[str] = list()

        for letter in word:
            if letter not in temp_list:
                temp_list.append(letter)

        new_dic: dict = dict()
        for i, j in enumerate(temp_list):
            new_dic[j] = str(i)


        temp: str = ""
        for i in word:
            temp += new_dic[i]

        return temp


solution = Solution()

print(solution.findAndReplacePattern(words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"))







