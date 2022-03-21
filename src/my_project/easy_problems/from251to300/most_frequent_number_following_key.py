from typing import List 
import collections

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        dic = collections.defaultdict(int)
        ans = float("inf")
        temp = 0
        for i in range(len(nums)-1):
            if nums[i] == key:
                dic[nums[i+1]] += 1
                if temp < dic[nums[i+1]]:
                    ans = nums[i+1]
                    temp = dic[nums[i+1]]
        
        return ans
        
        
        