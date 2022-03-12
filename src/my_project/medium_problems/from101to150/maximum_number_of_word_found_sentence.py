from typing import List 

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        answer: int = 0
        
        for sentence in sentences:
            if self.split_and_sum(sentence) > answer:
                answer = self.split_and_sum(sentence)
            
        
        return answer
    
    def split_and_sum(self, sentence: str) -> int:
        
        return len(sentence.split(" "))
    
    
    
solution = Solution()

print(solution.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))