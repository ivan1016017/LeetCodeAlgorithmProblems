from typing import List

class FirstSolution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        # initialize variables
        len_points = len(points)
        count = 0
        for i in range(len_points-1):
            count += self.countSeconds(points[i], points[i+1])

        return count

    def countSeconds(self, point_1, point_2) -> int:

        dist_x = abs(point_1[0]-point_2[0])
        dist_y = abs(point_1[1] - point_2[1])

        if dist_x < dist_y:
            return dist_x + (dist_y-dist_x)
        elif dist_y < dist_x:
            return dist_y + (dist_x-dist_y)
        else:
            return dist_x

# solution = FirstSolution()
# print(solution.minTimeToVisitAllPoints(points = [[3,2],[-2,2]]))


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        # initialize variables
        len_points = len(points)
        count = 0
        for i in range(len_points-1):
            dist_x = abs(points[i+1][0] - points[i][0])
            dist_y = abs(points[i+1][1] - points[i][1])
            count += max(dist_x, dist_y)

        return count

solution = Solution()
print(solution.minTimeToVisitAllPoints(points = [[3,2],[-2,2]]))


