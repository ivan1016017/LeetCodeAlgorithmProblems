from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        solution: int = 0

        ordered_heights = heights.copy()
        ordered_heights.sort()
        print(heights)
        print(ordered_heights)
        for i in range(len(heights)):
            if heights[i] != ordered_heights[i]:
                solution += 1

        return solution


solution = Solution()
print(solution.heightChecker(heights = [1,1,4,2,1,3]))