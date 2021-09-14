from typing import List 

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:

        arr.sort()

        solution: bool = True

        if len(arr) == 1:
            return solution

        temp = arr[1] - arr[0]
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i]  != temp:
                solution = False 
                return solution

        return solution 


solution = Solution()

print(solution.canMakeArithmeticProgression(arr = [1,2,4]))


