from typing import List


if __name__ == '__main__':
    class Solution:
        def searchInsert(self, nums: List[int], target: int) -> int:

            # initialize index variable
            index = len(nums)

            # loop through the array
            for i in range(len(nums)):

                if nums[i] == target:
                    index = i
                    return index
                elif nums[i] > target:
                    index = i
                    return index

            return index

    solution = Solution()
    print(solution.searchInsert([1],0))