function fib(n: number): number {
    if (n===0){
        return 0
    }

    let dp: Array<number> = Array(n+1).fill(0)
    dp[0] = 0
    dp[1] = 1

    for (let i = 2; i < n+1; i++){
        dp[i] = dp[i-1] + dp[i-2]
    }

    return dp[n]
};