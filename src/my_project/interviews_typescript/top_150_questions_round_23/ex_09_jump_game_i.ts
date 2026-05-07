function canJump(nums: number[]): boolean {
    const n = nums.length;

    // Base case: already at the end
    if (n === 1) return true;

    // dp[i] = 1 means position i can reach the end
    const dp: number[] = new Array(n).fill(0);

    // Start from the last index (our goal)
    let prevBest = n - 1;

    // Iterate backwards from second-to-last to first index
    for (let i = n - 2; i >= 0; i--) {
        // Maximum jump length from current position
        const step = nums[i];

        // Check if current position can reach any "good" position
        if (i + step >= prevBest) {
            // Mark this position as reachable to the end
            dp[i] = 1;

            // Update the leftmost position that can reach the end
            prevBest = i;
        }
    }

    // Check if we can reach the end from the start (index 0)
    return dp[0] === 1;
}

