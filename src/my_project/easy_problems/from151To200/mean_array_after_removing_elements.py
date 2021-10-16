from typing import List 

class Solution:
    def trimMean(self, arr: List[int]) -> float:

        arr.sort()

        index_smallest: int = int(0.05 * len(arr))
        index_largest: int = int(len(arr) - 0.05 * len(arr))
        new_list: List[int] = arr[index_smallest:index_largest]

        return sum(new_list)/len(new_list)

solution = Solution()

print(solution.trimMean(arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]))

print(solution.trimMean(arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]))

print(solution.trimMean(arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]))

print(solution.trimMean(arr = [9,7,8,7,7,8,4,4,6,8,8,7,6,8,8,9,2,6,0,0,1,10,8,6,3,3,5,1,10,9,0,7,10,0,10,4,1,10,6,9,3,6,0,0,2,7,0,6,7,2,9,7,7,3,0,1,6,1,10,3]))



