from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:

        # initialize variables
        target = list()
        len_index = len(index)

        for i in range(len_index):
            target.insert(index[i], nums[i])


        return target


solution = Solution()

print(solution.createTargetArray([0,1,2,3,4], [0,1,2,2,1]))





