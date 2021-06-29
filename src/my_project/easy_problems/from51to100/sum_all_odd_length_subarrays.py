from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:

        n = len(arr)
        solution = 0

        for i in range(n):
            solution += ((i + 1) * (n - i) + 1) // 2 * arr[i]

        return solution
