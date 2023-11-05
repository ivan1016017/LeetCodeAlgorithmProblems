let m, n
function numIslands(grid: string[][]): number {
    let count: number = 0
    if (!grid || !grid[0]) return count 
    m = grid.length
    n = grid[0].length
    for (let i = 0; i < m; i++) {
      for (let j = 0; j < n; j++) {
          if (grid[i][j] === "1") {
              count++
              dfs(grid, i, j)
          }
      }  
    }
    return count
};

function dfs(grid: string[][], i: number, j: number) {
    if (i >= m || j >= n || i < 0 || j < 0 || grid[i][j] === '0') return
    grid[i][j] = '0'
    dfs(grid, i + 1, j)
    dfs(grid, i - 1, j)
    dfs(grid, i, j - 1)
    dfs(grid, i, j + 1)
}