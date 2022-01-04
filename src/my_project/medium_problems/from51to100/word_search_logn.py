from typing import List 

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.backtracking(i,j,word,board):
                    return True 
        return False 
    
    
    def backtracking(self,i,j,word,board):
        if len(word) == 0:
            return True 
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False 
        if board[i][j] == word[0]:
            board[i][j] = "*"
            if self.backtracking(i-1,j,word[1:],board) or self.backtracking(i+1,j,word[1:],board) or self.backtracking(i,j-1,word[1:],board) or self.backtracking(i,j+1,word[1:],board):
                return True 
            board[i][j] = word[0]
        
        return False