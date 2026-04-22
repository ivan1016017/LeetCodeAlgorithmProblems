function uniquePathsWithObstacles(obstacleGrid: number[][]): number {
    const m = obstacleGrid.length;
    const n = obstacleGrid[0].length;
    if (obstacleGrid[0][0] === 1 || obstacleGrid[m - 1][n - 1] === 1) return 0;
    const dp: number[] = new Array(n).fill(0);
    dp[0] = 1;
    for (let row = 0; row < m; row++) {
        for (let col = 0; col < n; col++) {
            if (obstacleGrid[row][col] === 1) {
                dp[col] = 0;
            } else if (col > 0) {
                dp[col] += dp[col - 1];
            }
        }
    }
    return dp[n - 1];
};