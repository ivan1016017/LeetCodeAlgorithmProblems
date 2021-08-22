from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        solution = [[]]

        for number in nums:
            solution += [temp + [number] for temp in solution]

        return solution


solution = Solution()
# print(solution.subsets([1,2,3]))

