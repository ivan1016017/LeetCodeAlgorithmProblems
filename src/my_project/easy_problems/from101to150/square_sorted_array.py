from typing import List 

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        solution: List[int] = list()
        for num in nums:
            solution.append(num**2)
        solution.sort()
        return solution 


solution = Solution()

print(solution.sortedSquares(nums = [-4,-1,0,3,10]))