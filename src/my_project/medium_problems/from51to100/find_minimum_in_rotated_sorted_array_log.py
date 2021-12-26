from typing import List 


class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        low = 0
        high = len(nums) -1
        mid = 0
        while (low < high):
            mid = (low + high)//2
            
            if (nums[mid] < nums[mid-1]   and nums[mid] < nums[mid+1]):
                return nums[mid]
            
            elif nums[mid] < nums[high]:
                high = mid -1
                
            elif nums[mid] > nums[high]:
                low = mid + 1
            
        
        return nums[low]