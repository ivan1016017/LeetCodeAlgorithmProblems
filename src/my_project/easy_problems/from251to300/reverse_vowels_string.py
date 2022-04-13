from typing import List 

class Solution:
    def reverseVowels(self, s: str) -> str:
        
   
        ind_vec = []
        for index,char in enumerate(s):
            if char in ['a','e','i','o','u','A','E','I','O','U']:
                ind_vec.append(index)
        N = len(ind_vec)
        
        s_copy = [letter for letter in s]
        for i in range(len(ind_vec)):
            s_copy[ind_vec[i]] = s[ind_vec[N-1-i]]
            
        

        
        
        return ''.join(s_copy)