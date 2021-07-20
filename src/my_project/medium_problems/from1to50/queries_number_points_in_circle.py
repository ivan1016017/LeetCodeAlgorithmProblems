from typing import List

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:

        # initialize variables
        count = 0
        solution = list()

        for query in queries:
            count = 0
            for point in points:
                if abs(((point[0]-query[0])**2) + ((point[1]-query[1])**2 ) )<= query[2]:
                    count += 1
            solution.append(count)


        return solution


solution = Solution()
print(solution.countPoints(points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]))
