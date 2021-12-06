from typing import List 

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        
        count_ones = 0
        count_zeroes = 0
        max_ones = 0
        max_zeroes = 0
        len_s: int = len(s)
        answer: bool = False
        
        
        if len_s == 1:
            if s == "1":
                answer = True 
                return answer 
            else: 
                return answer 
            
        s = s + "a"
        len_s += 1
        
        for i in range(len(s)-1):
            
            if s[i] =="1":
                count_ones +=1 
                if s[i+1] == "1":
                    continue
                else:
                    if count_ones > max_ones:
                        max_ones = count_ones
                        count_ones = 0
                    else: count_ones = 0          
            elif s[i] == "0": 
                count_zeroes +=1 
                
                if s[i+1] == "0":
                    continue
                else:
                    if count_zeroes > max_zeroes:
                        max_zeroes = count_zeroes
                        count_zeroes = 0
                    else: 
                        count_zeroes = 0
              
        if max_ones > max_zeroes:
            answer = True     
        
        return answer 
    
solution = Solution()

print(solution.checkZeroOnes(s = "1101"))

print(solution.checkZeroOnes( s = "111000"))

print(solution.checkZeroOnes(s = "110100010"))
