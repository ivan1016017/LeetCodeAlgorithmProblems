from typing import List 

class Solution:
    def getLucky(self, s: str, k: int) -> int:
       
        
        def sum_digits(num: int) -> int:
            
            answer = 0
            quotient = 0
            
            num_to_string = str(num)
            len_num = len(num_to_string)
            
            for i in range(len_num):
                quotient = num // (10**(len_num -1 - i))
                answer += quotient
                num = num % (10**(len_num -1 - i))
                
            
            return answer 

                
        len_s = len(s)
        temp = ""       
        for i in range(len_s):
            temp += str(ord(s[i]) -96)
            
        print(temp)      
            
        answer = int(temp)
        
        print(answer)
            
        for l in range(k):
            answer = sum_digits(answer)
        
        
        return answer
    
    

solution = Solution()

# print(solution.getLucky(s = "iiii", k = 1))

# print(solution.getLucky( s = "leetcode", k = 2))

# print(solution.getLucky(s = "zbax", k = 2))

print(solution.getLucky("dbvmfhnttvr", 5))

