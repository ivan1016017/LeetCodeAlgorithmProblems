from typing import List

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:

        solution = True



        print(target)
        target.sort()
        arr.sort()
        print(arr)
        len_target = len(target)

        for i in range(len_target):
            if target[i] != arr[i]:
                solution = False
                break


        return solution


solution = Solution()

print(solution.canBeEqual(target = [1,2,3,4], arr = [2,4,1,3]))