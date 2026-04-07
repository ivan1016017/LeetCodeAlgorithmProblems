function singleNumber(nums: number[]): number {
    return nums.reduce((acc, n) => acc ^ n, 0);
};