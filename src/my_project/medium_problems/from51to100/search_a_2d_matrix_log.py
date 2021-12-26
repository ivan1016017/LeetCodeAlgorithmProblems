from typing import List 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = []
        
        for list_nums in matrix:
            nums = nums + list_nums
        
        def binarySearch(nums: List[int], left: int, right: int, target:int) -> bool:
            if left > right:
                return False 

            mid = (left + right) // 2 

            if nums[mid] == target:
                return True

            if nums[left] <= nums[mid]:

                if target >= nums[left] and target <= nums[mid]:
                    return binarySearch(nums, left, mid-1,target)
                return binarySearch(nums, mid + 1, right, target)

            if target >= nums[mid] and target <= nums[right]:
                return binarySearch(nums, mid + 1, right, target)
            return binarySearch(nums, left, mid -1,target)


        return binarySearch(nums, 0, len(nums)-1, target)

