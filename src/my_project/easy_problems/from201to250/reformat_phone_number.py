from typing import List 

class Solution:
    def reformatNumber(self, number: str) -> str:
        
        
        temp = number.replace(' ','').replace('-','')
        
        answer = []
        
        count = 0
        while count < len(temp):
            if len(temp)-count == 4:
                answer.append(temp[count:count+2])
                answer.append(temp[count+2:count+4])
                break 
            if len(temp) - count  == 3:
                answer.append(temp[count: count+3])
                break 
            if len(temp) - count  == 2:
                answer.append(temp[count:count+2])
                break 
            answer.append(temp[count:count+3])
            count += 3
        
        return '-'.join(answer)
    
    
solution = Solution()

print(solution.reformatNumber(number = "1-23-45 6"))

print(solution.reformatNumber(number = "123 4-567"))

print(solution.reformatNumber(number = "123 4-5678"))

print(solution.reformatNumber(number = "12"))

print(solution.reformatNumber(number = "--17-5 229 35-39475 "))