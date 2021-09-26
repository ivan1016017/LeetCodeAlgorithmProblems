from typing import List 

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:

        answer: List[int] = list()
        answer = points.copy()
        flag: bool = False
        for item in points:
            if item[0] == x or item[1] == y:
                flag = True 
        
        if flag == False:
            return -1
        
    
        def distance_manhattan(point: List[int]):
            return abs(point[0] - x) + abs(point[1] - y)

        points.sort(key= lambda point: distance_manhattan(point))
        print(points)
        return answer.index(points[0])

solution = Solution()

print(solution.nearestValidPoint(x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]))

print(solution.nearestValidPoint(x = 3, y = 4, points = [[2,3]]))

print(solution.nearestValidPoint(5,1 ,[[1,1],[6,2],[1,5],[3,1]]))

