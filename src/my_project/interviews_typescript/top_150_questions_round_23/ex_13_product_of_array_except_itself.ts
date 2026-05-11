function productExceptSelf(nums: number[]): number[] {
    const n = nums.length;
    const answer: number[] = new Array(n).fill(1);

    // First pass: prefix products
    let prefix = 1;
    for (let i = 0; i < n; i++) {
        answer[i] = prefix;
        prefix *= nums[i];
    }

    // Second pass: suffix products multiplied in-place
    let suffix = 1;
    for (let i = n - 1; i >= 0; i--) {
        answer[i] *= suffix;
        suffix *= nums[i];
    }

    return answer;
};        