from typing import List 

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        coordinate_rook = []
        number_pawns = 0
        

        for i in range(8):
            for j in range(8):

                if board[i][j] == "R":
                    coordinate_rook = [i,j]
        flag = False
        for i in range(coordinate_rook[0]-1, -1, -1):
            if board[i][coordinate_rook[1]] != "." and  board[i][coordinate_rook[1]] != "p":
                flag = True 
            if flag == False and board[i][coordinate_rook[1]] == "p":
                number_pawns +=1
                flag = True


        flag = False
        for i in range(coordinate_rook[0] + 1, 8):
            if board[i][coordinate_rook[1]] != "." and  board[i][coordinate_rook[1]] != "p":
                flag = True 
            if flag == False and board[i][coordinate_rook[1]] == "p":
                number_pawns +=1
                flag = True

        flag = False
        for j in range(coordinate_rook[1]-1, -1, -1):
            if board[coordinate_rook[0]][j] != "." and  board[coordinate_rook[0]][j] != "p":
                flag = True 
            if flag == False and board[coordinate_rook[0]][j] == "p":
                number_pawns +=1
                flag = True
            
        flag = False
        for j in range(coordinate_rook[1]+1, 8):
            if board[coordinate_rook[0]][j] != "." and  board[coordinate_rook[0]][j] != "p":
                flag = True 
            if flag == False and board[coordinate_rook[0]][j]== "p":
                number_pawns +=1
                flag = True





        return number_pawns  

solution = Solution()

print(solution.numRookCaptures(board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]))

print(solution.numRookCaptures(board = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]))