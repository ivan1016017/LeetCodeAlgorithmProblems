from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Find the starting and ending position of a target value in a sorted array.
        Time Complexity: O(log n) using binary search
        Space Complexity: O(1)
        """
        if not nums:
            return [-1, -1]
        
        # Find the leftmost (first) occurrence
        left = self.findLeft(nums, target)
        if left == -1:
            return [-1, -1]
        
        # Find the rightmost (last) occurrence
        right = self.findRight(nums, target)
        
        return [left, right]
    
    def findLeft(self, nums: List[int], target: int) -> int:
        """Find the leftmost occurrence of target"""
        left, right = 0, len(nums) - 1
        result = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                result = mid
                right = mid - 1  # Continue searching in the left half
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    def findRight(self, nums: List[int], target: int) -> int:
        """Find the rightmost occurrence of target"""
        left, right = 0, len(nums) - 1
        result = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                result = mid
                left = mid + 1  # Continue searching in the right half
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
        