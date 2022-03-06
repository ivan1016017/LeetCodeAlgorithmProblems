function minDistance(word1: string, word2: string): number {

    let m: number = word1.length
    let n: number = word2.length
    let dp: Array<Array<number>>=[]

    dp.push([...Array(n+1).keys()])
    for (let r =0; r < m; r++){
        dp.push([r+1].concat(Array(n).fill(0)))
    }

    for (let i = 0; i < m; i++){
        for (let j = 0; j<n; j++){
            if (word1[i]===word2[j]){
                dp[i+1][j+1]=dp[i][j]
            }
            else{
                dp[i+1][j+1] = Math.min(dp[i][j],dp[i+1][j],dp[i][j+1]) +1
            }
        }
    }

    return dp[m][n]
};