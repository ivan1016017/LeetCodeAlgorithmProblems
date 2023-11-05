function lengthOfLIS(nums: number[]): number {

    if (!nums){
        return 0
    }

    let lenNums: number = nums.length

    let dp: Array<number> = Array(lenNums).fill(1)


    for (let i = 1; i < lenNums; i++){
        for (let j = 0; j < i; j++){
            if (nums[i] > nums[j]){
                dp[i] = Math.max(dp[i], 1+dp[j])
            }
        }
    }


    return dp.reduce( (a,b) => Math.max(a,b),0)
};

console.log(lengthOfLIS([10,9,2,5,3,7,101,18]))