function removeDuplicates(nums: number[]): number {
    let j = 0;
    const lenNums = nums.length;

    for (let i = 0; i < lenNums - 1; i++) {
        if (nums[i] !== nums[i + 1]) {
            nums[j] = nums[i];
            j++;
        }
    }

    nums[j] = nums[lenNums - 1];

    return j + 1;
};