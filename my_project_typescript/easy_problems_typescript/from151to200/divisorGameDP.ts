function divisorGame(n: number): boolean {

    let dp: Array<boolean> = Array(n+1).fill(false)

    for (let i = 0; i < n+1; i++){
        for (let j = 1; j < Math.floor(n/2) + 1; j++){
            if (i%j === 0 && !dp[i-j]){
                dp[i] = true 
                break 
            }
        }
    }

    return dp[n]
};