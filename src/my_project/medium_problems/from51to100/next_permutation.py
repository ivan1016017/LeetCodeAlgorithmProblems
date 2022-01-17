from socket import NI_NUMERICHOST
from typing import List 


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:   # nums are in descending order
            nums.reverse()
            return 
        k = i - 1    # find the last "ascending" position
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]  
        print(nums, 'sdfsdf')
        l, r = k+1, len(nums)-1  # reverse the second part
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            print(nums)
            l +=1 ; r -= 1
            
            
            
solution = Solution()

print(solution.nextPermutation([1,2,4,3]))
print(solution.nextPermutation([1,3,2,4]))
