function trailingZeroes(n: number): number {
    // Count trailing zeroes in n! by counting factors of 5
    // Trailing zeroes come from 10 = 2 * 5
    // Since there are always more factors of 2 than 5 in n!,
    // we just need to count factors of 5
    // 
    // We count: floor(n/5) + floor(n/25) + floor(n/125) + ...
    // Time: O(log n), Space: O(1)
    
    let count = 0;
    while (n > 0) {
        n = Math.floor(n / 5);
        count += n;
    }
    return count;
};

