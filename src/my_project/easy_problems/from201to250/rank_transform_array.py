from typing import List 

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        
        ordered_list = list()
        len_arr = len(arr)
        temp_dict = dict()
        
        for i in range(len_arr):
            temp_dict[arr[i]]= 0
            
        for i in temp_dict.keys():
    
            ordered_list.append(i)
            
        ordered_list.sort()
        
        solution_dict = dict()
        value_index = 1        
        for i in ordered_list: 
            solution_dict[i] = value_index 
            value_index += 1
            
        for i in range(len_arr):
            arr[i] = solution_dict[arr[i]]
        
        return arr
    
solution = Solution()

print(solution.arrayRankTransform(arr = [40,10,20,30]))

print(solution.arrayRankTransform(arr = [100,100,100]))

print(solution.arrayRankTransform(arr = [37,12,28,9,100,56,80,5,12]))
