from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Search for target in a rotated sorted array using binary search.
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        
        Args:
            nums: Rotated sorted array with distinct values
            target: Target value to search for
            
        Returns:
            Index of target if found, -1 otherwise
        """
        if not nums:
            return -1
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Found target
            if nums[mid] == target:
                return mid
            
            # Determine which half is sorted
            if nums[left] <= nums[mid]:
                # Left half is sorted
                if nums[left] <= target < nums[mid]:
                    # Target is in the sorted left half
                    right = mid - 1
                else:
                    # Target is in the right half
                    left = mid + 1
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    # Target is in the sorted right half
                    left = mid + 1
                else:
                    # Target is in the left half
                    right = mid - 1
        
        return -1
