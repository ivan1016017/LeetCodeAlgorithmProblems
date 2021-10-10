from typing import List 

class Solution:
    def arraySign(self, nums: List[int]) -> int:

        count: int = 1
        

        for number in nums: 
            count *= number

        if count == 0:
            return 0

        if count > 1:
            return 1

        if count < 1:
            return -1

    

        


        


solution = Solution()

print(solution.arraySign(nums = [-1,-2,-3,-4,3,2,1]))

print(solution.arraySign(nums = [1,5,0,2,-3]))

print(solution.arraySign(nums = [-1,1,-1,1,-1]))
