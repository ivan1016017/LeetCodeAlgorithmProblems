function rob(nums: number[]): number {
    /**
     * Dynamic Programming approach:
     * - For each house, we choose max of:
     *   1. Rob current house + max money from i-2 houses
     *   2. Skip current house and take max money from i-1 houses
     * 
     * Time: O(n), Space: O(1)
     */
    if (nums.length === 0) return 0;
    if (nums.length === 1) return nums[0];
    
    // prev2: max money robbed up to i-2
    // prev1: max money robbed up to i-1
    let prev2 = nums[0];
    let prev1 = Math.max(nums[0], nums[1]);
    
    for (let i = 2; i < nums.length; i++) {
        const current = Math.max(nums[i] + prev2, prev1);
        prev2 = prev1;
        prev1 = current;
    }
    
    return prev1;
}

// Example usage:
// console.log(rob([1, 2, 3, 1]));      // Output: 4
// console.log(rob([2, 7, 9, 3, 1]));   // Output: 12