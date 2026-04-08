function singleNumberII(nums: number[]): number {
    let ones = 0, twos = 0;
    for (const n of nums) {
        ones = (ones ^ n) & ~twos;
        twos = (twos ^ n) & ~ones;
    }
    return ones;
};