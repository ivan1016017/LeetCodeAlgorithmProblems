from typing import List 

class Solution:
    def judgeCircle(self, moves: str) -> bool:


        coordinate_position = {'L':-1, 'R':1, 'U':1,'D':-1}

        final_position: list[int] = [0,0]

        for move in moves: 
            if move == 'L' or move == 'R':
                final_position[0] += coordinate_position[move]
            else: 
                final_position[1] += coordinate_position[move]
                
        
        return final_position[0] == 0 and final_position[1] == 0

solution = Solution()

print(solution.judgeCircle(moves = "UD"))

print(solution.judgeCircle(moves = "LL"))


print(solution.judgeCircle(moves = "RRDD"))

print(solution.judgeCircle(moves = "LDRRLRUULR"))
