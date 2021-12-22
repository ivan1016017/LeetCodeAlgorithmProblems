from typing import List 

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        answer: str = ""
        def isPalindrome(word: str) -> bool:
            
            answer: bool = True
            len_word: int = len(word)
            for i in range(len_word//2):
                if word[i] != word[len_word-1-i]:
                    answer = False
                    return answer
            return answer 
        
        for word in words:
            if isPalindrome(word):
                answer = word
                return answer
        
        return answer
    
solution = Solution()

print(solution.firstPalindrome(words = ["abc","car","ada","racecar","cool"]))

print(solution.firstPalindrome(words = ["notapalindrome","racecar"]))

print(solution.firstPalindrome(words = ["def","ghi"]))

    
