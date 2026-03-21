function maxSubarraySumCircular(nums: number[]): number {
    let total = 0;
    let maxSum = nums[0];
    let curMax = 0;
    let minSum = nums[0];
    let curMin = 0;

    for (const num of nums) {
        curMax = Math.max(curMax + num, num);
        maxSum = Math.max(maxSum, curMax);
        curMin = Math.min(curMin + num, num);
        minSum = Math.min(minSum, curMin);
        total += num;
    }

    if (maxSum > 0) {
        return Math.max(maxSum, total - minSum);
    }
    return maxSum;
};