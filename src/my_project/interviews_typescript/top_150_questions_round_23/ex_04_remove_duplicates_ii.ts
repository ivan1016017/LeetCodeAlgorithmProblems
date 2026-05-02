function removeDuplicates(nums: number[]): number {
    const n = nums.length;

    if (n < 3) return n;

    let i = 1, j = 2;

    while (j < n) {
        if (nums[i - 1] !== nums[j]) {
            i++;
        }

        nums[i] = nums[j];
        j++;
    }

    return i + 1;
};