from typing import List 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        def binarySearch(nums: List[int], left: int, right: int, target:int) -> int:
            if left > right:
                return -1 
            
            mid = (left + right) // 2 
            
            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                
                if target >= nums[left] and target <= nums[mid]:
                    return binarySearch(nums, left, mid-1,target)
                return binarySearch(nums, mid + 1, right, target)
            
            if target >= nums[mid] and target <= nums[right]:
                return binarySearch(nums, mid + 1, right, target)
            return binarySearch(nums, left, mid -1,target)
        
        
        return binarySearch(nums, 0, len(nums)-1, target)
    
    
solution = Solution()

print(solution.search(nums = [4,5,6,7,0,1,2], target = 0))

print(solution.search(nums = [4,5,6,7,0,1,2], target = 3))

print(solution.search(nums = [1], target = 0))

