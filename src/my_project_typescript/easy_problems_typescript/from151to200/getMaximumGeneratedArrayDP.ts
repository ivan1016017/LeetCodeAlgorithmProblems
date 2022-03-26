function getMaximumGenerated(n: number): number {

    if (n === 0){
        return 0
    }
    else if (n === 1 || n === 2){
        return 1
    }

    let dp: Array<number> = Array(n+1).fill(0)
    dp[0] = 0
    dp[1] = 1
    let count: number = 2
    let check: number = 1
    let num: number = 1

    while (count <= n){
        if (check === 1 && count <= n){
            dp[num*2] = dp[num]
            check += 1
            count += 1
        }
        if (check === 2 && count <= n){
            dp[(num*2) + 1] = dp[num] + dp[num+1]
            check = 1
            num += 1
            count += 1
        }
        else{
            count += 1
        }
    }

    return Math.max.apply(null,dp)

};