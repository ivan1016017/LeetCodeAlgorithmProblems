from typing import List 

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def checkNice(s:str)-> bool:
            dict_answer = dict()
            answer = True
            for letter in s:
                dict_answer[letter] = 0
                if ord(letter) <= 90 and ord(letter) >= 65:
                    dict_answer[chr(ord(letter) + 32)] = 0
                else: 
                    dict_answer[chr(ord(letter) - 32)] = 0
                    
            for letter in s: 
                dict_answer[letter] += 1
                
            for letter in s:
                if ord(letter) <= 90 and ord(letter) >= 65:
                    if dict_answer[chr(ord(letter) + 32)] == 0:
                        answer = False 
                        return answer
                else: 
                    if dict_answer[chr(ord(letter) - 32)] == 0:
                        answer = False 
                        return answer       
                    
            return answer 
        
        len_s = len(s)
        max = -1
        answer: str = ""
        
        for i in range(len_s):
            for j in range(i+1, len_s):
                if checkNice(s[i:j+1]) and (len(s[i:j+1]) > max):
                    answer = s[i:j+1]
                    max = len(s[i:j+1])    
        return answer 
    
    
solution = Solution()

print(solution.longestNiceSubstring(s = "YazaAay"))

print(solution.longestNiceSubstring(s = "Bb"))

print(solution.longestNiceSubstring( s = "c"))

print(solution.longestNiceSubstring( s = "dDzeE"))


    
