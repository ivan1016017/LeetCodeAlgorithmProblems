function numDecodings(s: string): number {

    if (s[0] === "0"){
        return 0
    }

    let lenS: number = s.length

    let dp: Array<number> = Array(lenS + 1).fill(0)
    dp[0] = 1
    dp[1] = 1

    for (let i = 2; i < lenS + 1; i++){
        if (10 <= parseInt(s.slice(i-2,i)) && parseInt(s.slice(i-2,i)) <=26 ){
            dp[i] += dp[i-2]
        }
        if (1 <= parseInt(s[i-1]) && parseInt(s[i-1]) <=9 ){
            dp[i] += dp[i-1]
        }
    }
    
    return dp[lenS]

};