function canJump(nums: number[]): boolean {

    let n: number = nums.length

    if (n === 1 ){
        return true
    }

    let dp: Array<number> = Array(n).fill(0)

    let prevBest: number = n-1 
    let step:number 
    dp[n-1] = 1 

    for (let i = n-2; i>-1; i--){
        step = nums[i]

        if ( i+step >= prevBest){
            dp[i] = 1 
            prevBest = i
        }
    }

    console.log(dp)

    if (dp[0] === 1){
        return true
    }
    return false
};

console.log(canJump([1,0,1,0]))