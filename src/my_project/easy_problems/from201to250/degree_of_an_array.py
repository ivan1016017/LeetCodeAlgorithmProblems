from typing import List 

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        visited = {}
        
        for index, value in enumerate(nums):
            if value in visited: 
                visited[value].append(index)
            else: 
                visited[value] = [index]
        
        max_length = 0
        
        for k in visited.keys():
            max_length = max(len(visited[k]), max_length)
            
        answer = []
        
        for value in visited.values():
            if len(value) == max_length:
                answer.append(value[-1] - value[0])
                
        return min(answer) + 1