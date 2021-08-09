class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        cnt = 0
        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] != 'X':
                    continue
                if i > 0 and board[i-1][j] == 'X':
                    continue
                if j > 0 and board[i][j-1] == 'X':
                    continue
                cnt += 1
        return cnt