function rotate(nums: number[], k: number): void {
    const lenNums = nums.length;
    k = k % lenNums;
    const rotated = [...nums.slice(lenNums - k), ...nums.slice(0, lenNums - k)];
    for (let i = 0; i < lenNums; i++) {
        nums[i] = rotated[i];
    }
};
