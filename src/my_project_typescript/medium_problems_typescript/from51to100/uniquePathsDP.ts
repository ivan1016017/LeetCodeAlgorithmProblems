function uniquePathsWithObstacles(obstacleGrid: number[][]): number {

    if (obstacleGrid.length == 0 || obstacleGrid[0].length == 0){
        return 0
    }

    let m: number = obstacleGrid.length
    let n: number = obstacleGrid[0].length

    let dp: Array<Array<number>> = []

    for (let i = 0; i < m; i++){
        dp.push(Array(n).fill(0))
    }

    if (obstacleGrid[0][0] === 0){
        dp[0][0] = 1
    }
    else {
        return 0
    }

    for (let i = 0; i < m; i++){
        for (let j = 0; j < n; j++){
            if (obstacleGrid[i][j] === 1){
                continue
            }
            if (i > 0){
                dp[i][j] += dp[i-1][j]
            }
            if (j > 0){
                dp[i][j] += dp[i][j-1]
            }
        }
    }
    return dp[m-1][n-1]

};