from typing import List 

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max = -1
        len_colors = len(colors)
        for i in range(len_colors):
            for j in range(i+1, len_colors):
                if abs(colors[i]-colors[j]) != 0:
                    if j-i> max:
                        max = j-i
        
        return max 
    
    
solution = Solution()

print(solution.maxDistance(colors = [1,1,1,6,1,1,1]))

print(solution.maxDistance(colors = [1,8,3,8,3]))

print(solution.maxDistance(colors = [0,1]))
