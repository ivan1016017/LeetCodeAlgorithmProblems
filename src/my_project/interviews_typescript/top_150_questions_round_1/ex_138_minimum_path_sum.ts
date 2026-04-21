function minPathSum(grid: number[][]): number {
    const m = grid.length, n = grid[0].length;
    const dp: number[][] = grid.map(row => [...row]);
    for (let i = 1; i < m; i++) dp[i][0] += dp[i - 1][0];
    for (let j = 1; j < n; j++) dp[0][j] += dp[0][j - 1];
    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            dp[i][j] += Math.min(dp[i - 1][j], dp[i][j - 1]);
        }
    }
    return dp[m - 1][n - 1];
};