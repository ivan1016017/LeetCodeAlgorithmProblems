from typing import List 

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        result = ""
        i = 0
        len_s = len(strs)
        
        if len_s == 0:
            return result 
        
        first_word = min(strs, key=len)
        bench_mark = len(first_word)
        
        while i < bench_mark:
            for word in strs:
                print(word, first_word)
                if first_word[i] != word[i]:
                    return result 
            result += first_word[i]
            i+=1
                
        return result
        
        
solution   = Solution()

print(solution.longestCommonPrefix(strs = ["dog","racecar","car"]))

print(min(["flower","flow","flight"], key=len))

print(min( ["dog","racecar","car"], key=len))