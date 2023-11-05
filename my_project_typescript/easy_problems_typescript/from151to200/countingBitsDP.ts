function countBits(n: number): number[] {

    if (n == 0){
        return [0]
    }

    let dp: Array<number> = Array(n+1).fill(0)
    dp[0] = 0
    dp[1] = 1

    for (let i = 2; i < n+1; i++){
        if (i % 2 === 0){
            dp[i] = dp[Math.floor(i/2)]
        }
        else {
            dp[i] = 1 + dp[Math.floor((i-1)/2)]
        }
    }
    return dp

};