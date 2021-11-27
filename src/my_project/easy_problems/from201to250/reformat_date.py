from typing import List 

class Solution:
    def reformatDate(self, date: str) -> str:
        
        temp_list = date.split()
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        temp_dict = dict()
        for i in range(12):
            temp_dict[months[i]] = i+1
    
        answer = ""
        
        day = temp_list[0]
        month = temp_list[1]
        year = temp_list[2]
        
        answer = f'{year}-{temp_dict[month]:0>2d}-{int(day[0:len(day)-2]):0>2d}'
        
        return answer
    
    
solution = Solution()

print(solution.reformatDate(date = "20th Oct 2052"))

print(solution.reformatDate(date = "6th Jun 1933"))

print(solution.reformatDate(date = "26th May 1960"))
