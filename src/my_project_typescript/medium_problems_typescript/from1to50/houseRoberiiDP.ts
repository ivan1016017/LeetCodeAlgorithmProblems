function rob(nums: number[]): number {
    if (nums.length == 1){
        return nums[0]
    }
    return Math.max(maxRob(nums.slice(1)), maxRob(nums.slice(0,nums.length-1)))
};

function maxRob(nums:number[]):number{
    if (!nums){
        return 0
    }
    if (nums.length <= 2){
        return Math.max.apply(null,nums)
    }
    let dp: Array<number> = Array(nums.length).fill(0)
    dp[0] = nums[0]
    dp[1] = Math.max(nums[0],nums[1])
    for (let i = 2; i < nums.length; i++){
        dp[i] = Math.max(dp[i-2]+nums[i], dp[i-1])
    }
    return dp[nums.length-1]
}