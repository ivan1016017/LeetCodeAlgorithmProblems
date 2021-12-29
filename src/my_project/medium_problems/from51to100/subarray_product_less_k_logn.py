from typing import List 

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        product = 1
        left = 0
        answer = 0
        
        for right in range(len(nums)):
            product *= nums[right]
            
            while product >= k and right >= left:
                product/=nums[left]
                left +=1
            answer+= right-left+1
        return answer 