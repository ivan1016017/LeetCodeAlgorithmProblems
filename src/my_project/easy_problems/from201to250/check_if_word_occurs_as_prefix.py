from typing import List 

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        list_sentence = sentence.split()
        len_sentence: int = len(list_sentence)
        len_search_word: int = len(searchWord)
        flag: bool = False 
        for i in range(len_sentence):
            flag = False 
            
            for j in range(len_search_word):
                if len(searchWord) <= len(list_sentence[i]):
                    if searchWord[j] != list_sentence[i][j]:
                        flag = True
                        continue
                else: 
                    flag = True
                    continue
            if flag == False: 
                return i + 1
        return -1
    
solution = Solution()

print(solution.isPrefixOfWord(sentence = "i love eating burger", searchWord = "burg"))

print(solution.isPrefixOfWord(sentence = "this problem is an easy problem", searchWord = "pro"))

print(solution.isPrefixOfWord(sentence = "i am tired", searchWord = "you"))

print(solution.isPrefixOfWord(sentence = "i use triple pillow", searchWord = "pill"))

print(solution.isPrefixOfWord(sentence = "hello from the other side", searchWord = "they"))




