from typing import List 


class SecondSolution:
    def maxScore(self, s: str) -> int:
        def countOnes(nums: str) -> int:
            len_nums: int = len(nums)
            count: int = 0
            for i in range(len_nums):
                if nums[i] == '1':
                    count += 1
            return count
                    
        def countZeroes(nums: str) -> int:
            len_nums: int = len(nums)
            count: int = 0
            for i in range(len_nums):
                if nums[i] == '0':
                    count += 1
            return count 
                    
        answer: int = 0
        
        len_s: int = len(s)
        
        for i in range(1,len_s):
            if (countZeroes(s[0:i]) + countOnes(s[i:])) > answer: 
                answer = (countZeroes(s[0:i]) + countOnes(s[i:]))
            
        
        return answer 
    
    
class Solution:
    def maxScore(self, s: str) -> int:
        
        len_s: int = len(s)
        temp: int = 0
        for i in range(len_s):
            if s[i] == '1':
                temp +=1
        
        answer: int = -1
        
        for i in range(len_s -1):
            if s[i] == '0':
                temp += 1
            else: 
                temp -= 1
            answer = max(answer,temp)
            
    
        return answer 
            
            
        
        return answer 

solution = Solution()

print(solution.maxScore(s = "011101"))

print(solution.maxScore( s = "00111"))

print(solution.maxScore( s = "1111"))



