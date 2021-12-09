from typing import List 

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        len_s = len(s)
        len_t = len(t)
        
        dict_s = dict()
        
        dict_t = dict()
        
        for i in range(len_t):
            dict_t[t[i]] = 0
            dict_s[t[i]] = 0
            
        for i in range(len_s):
            dict_s[s[i]] += 1
            
        for i in range(len_t):
            dict_t[t[i]] += 1
            
        for key in dict_s:
            if dict_s[key] != dict_t[key]:
                return key
            
            
            
        
        return ""
    
solution = Solution()

print(solution.findTheDifference(s = "abcd", t = "abcde"))

print(solution.findTheDifference(s = "", t = "y"))

print(solution.findTheDifference(s = "a", t = "aa"))

print(solution.findTheDifference( s = "ae", t = "aea"))
