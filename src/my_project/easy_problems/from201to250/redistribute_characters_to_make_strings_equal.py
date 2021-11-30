from typing import List 

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
    
        temp_dict = dict()
        answer = True    
        vocab = ""
        for word in words:
            vocab = vocab + word
            
        len_vocab: int = len(vocab)
            
        for i in range(len_vocab):
            temp_dict[vocab[i]] = 0
        
        for i in range(len_vocab):
            temp_dict[vocab[i]] += 1
            
        len_words: int = len(words)
        
        for i in range(len_vocab):
            if temp_dict[vocab[i]] % len_words != 0:
                answer = False 
                return answer 
        
        
        return answer  
    
solution = Solution()

print(solution.makeEqual(words = ["abc","aabc","bc"]))

print(solution.makeEqual(words = ["ab","a"]))
