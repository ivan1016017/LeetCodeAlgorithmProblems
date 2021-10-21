from typing import List 

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        count: int = 0

        for num in arr:

            if num % 2 == 0:
                count = 0
            else: 
                count += 1
            if count >= 3:
                return True

        return False 

solution = Solution()

print(solution.threeConsecutiveOdds(arr = [2,6,4,1]))

print(solution.threeConsecutiveOdds(arr = [1,2,34,3,4,5,7,23,12]))
