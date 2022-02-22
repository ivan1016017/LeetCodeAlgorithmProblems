from typing import List 

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        ret = []
        self.dfs(sorted(nums), [], ret)
        return ret
    
    def dfs(self, nums, path, ret):
        ret.append(path)
        for i in range(len(nums)):
            print(ret)
            
            if i > 0 and nums[i] == nums[i-1]:
                print(ret, "condition hold")
                continue
            self.dfs(nums[i+1:], path+[nums[i]], ret)
            
        
solution = Solution()

solution.subsetsWithDup([1,2,2])
        
