from typing import List

class Solution:

    def algo_1(self, nums: List[int]):

        
        nums = [n for n in nums if n % 7 == 0]
        

        return len(nums), nums
    


solution = Solution()

print(solution.algo_1(nums=[1,2,7,14,34,35]))