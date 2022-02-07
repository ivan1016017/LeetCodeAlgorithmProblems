from typing import List 

class Solution(object):
    def productExceptSelf(self, nums):
        output = [1] * len(nums)
        
        # multiply by the left side
        left_product = 1
        for i in range(1, len(nums)):
            left_product *= nums[i-1]
            output[i] = left_product
        
        # multiply by the right side
        right_product = 1
        for i in range(len(nums)-2, -1, -1):
            right_product *= nums[i+1]
            output[i] *= right_product
        
        return output