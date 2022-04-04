from typing import List 

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        answer = ""
        j = 0
        
        min_word = min(strs, key=len)
        benchmark = len(min_word)
        
        while j < benchmark:
            for word in strs:
                if word[j] != min_word[j]:
                    return answer 
            answer = answer + min_word[j]
            j+=1
            
        
        
        return answer 
        
        
solution = Solution()

print(solution.longestCommonPrefix(["flower","flow","flight"]))