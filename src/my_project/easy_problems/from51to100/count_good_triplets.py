from typing import List

class SecondSolution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:


        len_arr = len(arr)
        count = 0

        for i in range(len_arr):
            for j in range(i+1, len_arr):
                for k in range(j+1, len_arr):
                    if abs(arr[i]-arr[j]) <= a and abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                        count += 1

        return count



class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j+1, len(arr)):
                        if (abs(arr[j] - arr[k]) <= b) and (abs(arr[i] - arr[k]) <= c):
                            count += 1
        return count

solution = Solution()
print(solution.countGoodTriplets(arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3))


