from typing import List 
from collections import deque 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m: int = len(grid)
        n: int = len(grid[0])
        num_islands: int = 0
        
        def bfs(i,j):
            queue = deque() 
            queue.append([i,j])
            
            while queue:
                
                for _ in range(len(queue)):
                    i, j = queue.popleft()
                    
                    for x, y in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                        # exploring the whole island
                        if x>=0 and x<m and y>=0 and y<n and grid[x][y]=='1':
                            queue.append([x,y])
                            grid[x][y]='in land'
                            
        for i in range(m):
            for j in range(n):
                 #visiting new islands
                if grid[i][j] !='in land' and grid[i][j] == '1':
                    grid[i][j]='in land'
                    bfs(i,j)
                    num_islands+=1
                     
        
        return num_islands
    
    
solution = Solution()

print(solution.numIslands( grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))