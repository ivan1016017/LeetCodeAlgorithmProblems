from typing import List 

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        index_list  = list()
        len_nums = len(nums)
        for i in range(len_nums):
            if nums[i] == target:
                index_list.append(i)

        
        
        index_list.sort(key= lambda x: abs(x-start) )
            
        return abs(index_list[0] - start)
    
    
    
solution = Solution()

print(solution.getMinDistance( nums = [1,2,3,4,5], target = 5, start = 3))

print(solution.getMinDistance( nums = [1], target = 1, start = 0))

print(solution.getMinDistance( nums = [1,1,1,1,1,1,1,1,1,1], target = 1, start = 0))