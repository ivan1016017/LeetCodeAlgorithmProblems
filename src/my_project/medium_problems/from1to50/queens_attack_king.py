from typing import List

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:


        directions = [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[1,-1], [-1,1],[1,1]]
        taken_directions = list()

        solution = list()
        for i in range(1,8):
            directions = [item for item in directions if item not in taken_directions ]
            for direction in directions:
                if [king[0] + direction[0]*i, king[1] + direction[1]*i] in queens:
                    solution.append([king[0] + direction[0]*i, king[1] + direction[1]*i])
                    taken_directions.append(direction)


        return solution


solution = Solution()

print(solution.queensAttacktheKing(queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]))

directions = [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[1,-1], [-1,1],[1,1]]

print(directions)
directions.remove([-1,0])
print(directions)