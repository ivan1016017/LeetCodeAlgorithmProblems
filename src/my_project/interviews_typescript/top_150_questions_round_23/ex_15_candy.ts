function candy(ratings: number[]): number {
    const n = ratings.length;
    if (n === 0) return 0;

    // Initialize all children with 1 candy
    const candies: number[] = new Array(n).fill(1);

    // Left-to-right pass: Compare with left neighbor
    for (let i = 1; i < n; i++) {
        if (ratings[i] > ratings[i - 1]) {
            candies[i] = candies[i - 1] + 1;
        }
    }

    // Right-to-left pass: Compare with right neighbor
    for (let i = n - 2; i >= 0; i--) {
        if (ratings[i] > ratings[i + 1]) {
            candies[i] = Math.max(candies[i], candies[i + 1] + 1);
        }
    }

    return candies.reduce((sum, c) => sum + c, 0);
}