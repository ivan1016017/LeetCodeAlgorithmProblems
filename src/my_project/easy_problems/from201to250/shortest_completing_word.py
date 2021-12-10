from typing import List 
import re 
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        words = sorted(words, key=len)
        string_filterd = ''.join(sorted([x for x in licensePlate.lower() if 97 <= ord(x) and ord(x) <= 122]))
        
        for word in words:
            
            temp = ''.join(word)
            exists = True
            for char in string_filterd:
                if char not in temp: 
                    exists = False
                    break 
                else: 
                    if temp.count(char) < string_filterd.count(char):
                        exists = False 
                        break 
            if exists: 
                return word
        return ""
    
    
soluiton = Solution()

print(soluiton.shortestCompletingWord(licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]))