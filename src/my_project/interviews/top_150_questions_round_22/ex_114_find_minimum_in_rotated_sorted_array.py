from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Find the minimum element in a rotated sorted array.
        
        Time Complexity: O(log n) - binary search
        Space Complexity: O(1) - constant space
        
        Args:
            nums: A rotated sorted array of unique elements
            
        Returns:
            The minimum element in the array
        """
        left = 0
        right = len(nums) - 1
        
        # If array is not rotated or has only one element
        if nums[left] <= nums[right]:
            return nums[left]
        
        while left < right:
            mid = left + (right - left) // 2
            
            # If mid element is greater than rightmost element,
            # the minimum must be in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # The minimum is in the left half (including mid)
                right = mid
        
        return nums[left]