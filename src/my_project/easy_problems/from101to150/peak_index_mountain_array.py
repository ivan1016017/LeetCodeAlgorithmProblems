from typing import List 

class SecondSolution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        arr_copy: List[int] = arr.copy()
        arr_copy.sort()
        arr_max: int = arr_copy[-1]



        return arr.index(arr_max)



class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        max: int = -1 
        solution: int = 0
        for i in range(len(arr)):
            if arr[i] > max:
                max = arr[i]
                solution = i 
        return solution 


solution = Solution()
print(solution.peakIndexInMountainArray(arr = [0,2,1,0]))
print(solution.peakIndexInMountainArray(arr = [0,10,5,2]))
print(solution.peakIndexInMountainArray(arr = [3,4,5,1]))

