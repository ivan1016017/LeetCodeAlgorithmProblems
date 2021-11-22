from typing import List 

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        
        answer = True
        len_word = len(word1)   
        alphabet = "abcdefghijklmnopqrstuvwxyz"   
        
        # initialize the dictionaries to count letters
        dict_word1 = dict()
        dict_word2 = dict()
        
        for i in range(26):
            dict_word1[alphabet[i]] = 0
            dict_word2[alphabet[i]] = 0
            
        # count the letters in each word
        for i in range(len_word):
            dict_word1[word1[i]] += 1
            dict_word2[word2[i]] += 1
            
        # check the words are almost equivalent
        for i in range(len_word):
            if abs(dict_word1[word1[i]] - dict_word2[word1[i]] ) > 3:
                answer = False 
                return answer  
            
        for i in range(len_word):
            if abs(dict_word1[word2[i]] - dict_word2[word2[i]] ) > 3:
                answer = False 
                return answer       
        return answer 
    
solution = Solution()

print(solution.checkAlmostEquivalent(word1 = "aaaa", word2 = "bccb"))

print(solution.checkAlmostEquivalent(word1 = "abcdeef", word2 = "abaaacc"))

print(solution.checkAlmostEquivalent(word1 = "cccddabba", word2 = "babababab"))

