from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1,-1]
        if target not in nums:
            return result

        #initialize flag
        flag_left = False
        flag_right = False
        # loop through the element of the array
        for i in range(len(nums)):

            # trigger flag when target appears in list for the first time
            if nums[i] == target:
                flag_left = True
                result[0] = i
                break


        # loop through the element of the array
        for i in range(len(nums)-1,-1,-1):

            # trigger flag when target appears in list for the first time
            if nums[i] == target:
                flag_right = True
                result[-1] = i
                break

        if flag_left and flag_right:
            return result
        if flag_left and not flag_right:
            return [result[0],result[0]]
        if not flag_left and flag_right:
            return [result[-1],result[-1]]

solution = Solution()
print(solution.searchRange([1,2,3], 2))