function permute(nums: number[]): number[][] {
    const result: number[][] = [];
    
    function backtrack(current: number[], remaining: number[]): void {
        // Base case: no more numbers to add
        if (remaining.length === 0) {
            result.push([...current]);
            return;
        }
        
        // Try each remaining number as the next element
        for (let i = 0; i < remaining.length; i++) {
            // Choose: add remaining[i] to current permutation
            current.push(remaining[i]);
            // Explore: recurse with remaining numbers
            const newRemaining = remaining.slice(0, i).concat(remaining.slice(i + 1));
            backtrack(current, newRemaining);
            // Unchoose: backtrack
            current.pop();
        }
    }
    
    backtrack([], nums);
    return result;
};