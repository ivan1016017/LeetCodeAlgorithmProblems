from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:

        # initialize variables
        horizonal_list = list()

        for point in points:
            horizonal_list.append(point[0])


        horizonal_list.sort()

        max = 0
        len_horizontal = len(horizonal_list)
        for i in range(1,len(horizonal_list)):
            if horizonal_list[i] - horizonal_list[i-1] > max:
                max = horizonal_list[i] - horizonal_list[i-1]

        return max

solution = Solution()

print(solution.maxWidthOfVerticalArea(points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))