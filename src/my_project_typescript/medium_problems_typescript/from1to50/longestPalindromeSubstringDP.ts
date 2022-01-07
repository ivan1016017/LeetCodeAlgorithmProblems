function longestPalindrome(s: string): string {

    if (!s || s.length==0){
        return ''
    }

    let n: number = s.length
    let dp: Array<Array<boolean>> = []

    for (let i = 0; i < n; i++){
        dp.push(Array(n).fill(false))
    }

    for (let i = 0; i < n; i++){
        dp[i][i] = true
    }

    let answer: string = s.slice(0,1)

    for (let i =0; i < n; i++){
        for (let j = i-1; j > -1; j--){
            if (s[i] === s[j] && (i-j < 2 || dp[j+1][i-1])){
                dp[j][i] = true 
                if (i-j + 1 > answer.length){
                    answer = s.slice(j,i+1)
                }
            }
        }
    }

    return answer
};

