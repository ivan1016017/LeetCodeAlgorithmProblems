function minPathSum(grid: number[][]): number {

    let m: number = grid.length
    let n: number = grid[0].length

    let rec: Array<Array<number>> = []

    for (let i = 0; i < m; i++){
        rec.push(Array(n).fill(0))
    }

    rec[0][0] = grid[0][0]

    for (let j = 1; j < n; j++){
        rec[0][j]  = rec[0][j-1] + grid[0][j]
    }

    for (let i = 1; i < m; i++){
        rec[i][0] = rec[i-1][0] + grid[i][0]
    }

    for (let i = 1; i < m; i++){
        for (let j = 1; j < n; j++){
            rec[i][j] = Math.min(rec[i-1][j], rec[i][j-1]) + grid[i][j]
        }
    }

    return rec[m-1][n-1]

};