from typing import List 

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        
        temp_dict = {}
        
        for word in words1:
            if word not in temp_dict:
                temp_dict[word] = [1,0]
            else:
                temp_dict[word][0] += 1
        
        
        for word in words2:
            if word not in temp_dict:
                temp_dict[word] = [0,1]
            else: 
                temp_dict[word][1] += 1
                
        answer = 0
        for word in temp_dict:
            if temp_dict[word] == [1,1]:
                answer += 1
        return answer 
    
    
solution  = Solution()

print(solution.countWords(words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]))

print(solution.countWords(words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]))

print(solution.countWords(words1 = ["a","ab"], words2 = ["a","a","a","ab"]))
