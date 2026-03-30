from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Find the median of two sorted arrays using binary search.
        Time complexity: O(log(min(m, n)))
        Space complexity: O(1)
        """
        # Ensure nums1 is the smaller array for efficiency
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            # Partition nums1
            partition1 = (left + right) // 2
            # Partition nums2 such that left side has half the total elements
            partition2 = (m + n + 1) // 2 - partition1
            
            # Handle edge cases where partition is at the boundary
            max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            min_right1 = float('inf') if partition1 == m else nums1[partition1]
            
            max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            min_right2 = float('inf') if partition2 == n else nums2[partition2]
            
            # Check if we found the correct partition
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # If total length is even
                if (m + n) % 2 == 0:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
                else:
                    # If total length is odd
                    return max(max_left1, max_left2)
            elif max_left1 > min_right2:
                # Move partition1 to the left
                right = partition1 - 1
            else:
                # Move partition1 to the right
                left = partition1 + 1
        
        raise ValueError("Input arrays are not sorted")