from typing import List 

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        first_year_list = list()
        len_logs: int = len(logs)
        max: int = 1
        
        
        for i in range(len_logs):
            if logs[i][0] not in first_year_list:
                first_year_list.append(logs[i][0])
            
        first_year_list.sort()
        len_logs = len(first_year_list)
 
        
        dict_max_records = dict()
        
        for i in range(len_logs):
            dict_max_records[first_year_list[i]] = 0
            
        for i in range(len_logs):
            for interval in logs:
                if first_year_list[i] >= interval[0] and first_year_list[i] < interval[1]:
                    dict_max_records[first_year_list[i]] += 1
                    
        answer = first_year_list[0]
        
        for i in range(len_logs):
            if dict_max_records[first_year_list[i]] > max:
                max = dict_max_records[first_year_list[i]]
                answer = first_year_list[i] 
  
        
        return answer 
    
solution = Solution()

print(solution.maximumPopulation(logs = [[1993,1999],[2000,2010]]))

print(solution.maximumPopulation(logs = [[1950,1961],[1960,1971],[1970,1981]]))

print(solution.maximumPopulation([[1966,1968],[1954,2030],[1966,1994],[2030,2044],[1988,2036],[1977,2050],[2036,2046],[1989,2048],[2049,2050],[2008,2019],[2022,2031],[1970,2024],[1957,1996],[1991,2034],[1956,1996],[1959,1969],[2021,2050]]))
