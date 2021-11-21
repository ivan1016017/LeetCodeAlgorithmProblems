from typing import List 

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        # answer 
        answer = 0
        
        # dictionaty to add the total occurences of each word in text
        temp_dict = dict()
        
        len_text = len(text) 
        
        for word in "balon":
            temp_dict[word] = 0
        
        # calculate the many times each word appears in text
        for i in range(len_text):
            temp_dict[text[i]] = 0
        
        for i in range(len_text):
            temp_dict[text[i]] += 1     
            
        # the total amoung of occurrences of each letter to form the word balloon
        ballon_occurrences = []        
          
        ballon_occurrences.append(temp_dict['b'])
        ballon_occurrences.append(temp_dict['a'])
        ballon_occurrences.append(temp_dict['l']//2)
        ballon_occurrences.append(temp_dict['o']//2)
        ballon_occurrences.append(temp_dict['n'])
        
        answer = min(ballon_occurrences)        
        
        return answer 
    
solution = Solution()

print(solution.maxNumberOfBalloons(text = "nlaebolko"))

print(solution.maxNumberOfBalloons(text = "loonbalxballpoon"))

print(solution.maxNumberOfBalloons(text = "leetcode"))

print(solution.maxNumberOfBalloons(text = "lloo"))

