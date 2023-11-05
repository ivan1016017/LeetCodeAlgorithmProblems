function minCostClimbingStairs(cost: number[]): number {
    let l: number = cost.length
    let dp: Array<number> = Array(l+2).fill(0)

    for (let i = 3; i < l+2; i++){
        dp[i] = Math.min(dp[i-1]+cost[i-2], dp[i-2]+cost[i-3])
    }

    return dp[l+1]

};