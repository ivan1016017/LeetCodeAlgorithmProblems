class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        # DP solution 
        res = [[0.0 for _ in range(i)] for i in range(1, query_row + 2)]
        res[0][0] = poured
        
        for i in range(query_row):
            for j in range(len(res[i])):
                if res[i][j] > 1 :
                    res[i+1][j] += (res[i][j] - 1) / 2.0
                    res[i+1][j+1] += (res[i][j] - 1) / 2.0
        
        return res[query_row][query_glass] if res[query_row][query_glass] <= 1 else 1
    
    
class SecondSolution(object):
    def champagneTower(self, poured, query_row, query_glass):
        A = [[0] * k for k in range(1, 102)]
        A[0][0] = poured
        for r in range(query_row + 1):
            for c in range(r+1):
                q = (A[r][c] - 1.0) / 2.0
                if q > 0:
                    A[r+1][c] += q
                    A[r+1][c+1] += q

        return min(1, A[query_row][query_glass])
