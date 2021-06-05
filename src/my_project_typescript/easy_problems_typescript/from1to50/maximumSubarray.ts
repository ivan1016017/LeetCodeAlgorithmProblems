function maxSubArray(nums: number[]): number {
    let n: number = nums.length;
    let localMax: number = 0;
    let globalMax: number = -(10**10);

    for (let i = 0; i < n; i++){
        localMax = Math.max(nums[i], nums[i] + localMax);
        if (localMax > globalMax){
            globalMax = localMax
        }
    }
    return globalMax;
};

console.log(maxSubArray([5,4,-1,7,8]));