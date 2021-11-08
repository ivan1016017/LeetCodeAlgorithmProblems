from typing import List 

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        
        text_list = text.split()
        len_text: int = len(text_list)
        answer  = list()
        
        for i in range(len_text-2):
            
            
            if text_list[i] == first and text_list[i+1] == second:
                answer.append(text_list[i+2])
        
        
        return answer  
    
    
solution = Solution()

print(solution.findOcurrences(text = "alice is a good girl she is a good student", first = "a", second = "good"))

print(solution.findOcurrences(text = "we will we will rock you", first = "we", second = "will"))

print(solution.findOcurrences(text = "alice is a good girl she is a good", first = "a", second = "good"))


    
    
        