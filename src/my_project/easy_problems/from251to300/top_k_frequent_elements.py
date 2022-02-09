from operator import invert
from typing import List 
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        ans_dict = defaultdict(int)
        
        for num in nums:
            ans_dict[num] += 1
        
        
        set_nums = set(nums)
        nums_unique = list(set_nums)    
        nums_unique.sort(key= lambda num: ans_dict[num], reverse=True)
        
        
        
        return nums_unique[0:k]
        
        
solution = Solution()

print(solution.topKFrequent(nums = [1,1,1,2,2,3], k = 2))


        
        