function maxSubArray(nums: number[]): number {
    const n = nums.length;
    let localMaximum = 0;
    let globalMaximum = -Infinity;

    for (let i = 0; i < n; i++) {
        localMaximum = Math.max(nums[i], nums[i] + localMaximum);

        if (localMaximum > globalMaximum) {
            globalMaximum = localMaximum;
        }
    }

    return globalMaximum;
};