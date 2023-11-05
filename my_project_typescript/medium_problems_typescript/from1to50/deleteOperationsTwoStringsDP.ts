function minDistanceTwo(word1: string, word2: string): number {

    let n: number = word1.length + 1 
    let m: number = word2.length + 1

    let dp: Array<Array<number>> =[]

    for (let j = 0; j < n; j++){
        dp.push(Array(m).fill(0))
    }

    for (let i = 1; i <n; i++){
        for (let j = 1; j < m; j++){
            if (word1[i-1] == word2[j-1]){
                dp[i][j] = 1 + dp[i-1][j-1]
            }
            else{
                dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1])
            }
        }
    }

    return m + n -2 - (2*dp[n-1][m-1])

};

console.log(minDistanceTwo("leetcode","etco"))