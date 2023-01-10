function coinChange(coins: number[], amount: number): number {
    let dp = new Array(amount + 1);
    dp.fill(Number.MAX_VALUE);
    
    dp[0] = 0;
    for (let i = 1; i <= amount; i++) {
        for (let j = 0; j < coins.length; j++) {
            if (i - coins[j] >= 0) {
                dp[i] = Math.min(dp[i - coins[j]] + 1, dp[i]);
            }
        }
    }
    return dp[amount] === Number.MAX_VALUE ? -1 : dp[amount];

};