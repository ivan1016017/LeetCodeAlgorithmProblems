function combine(n: number, k: number): number[][] {
    const result: number[][] = [];
    
    function backtrack(start: number, current: number[]): void {
        // Base case: if we have k numbers, add to result
        if (current.length === k) {
            result.push([...current]);
            return;
        }
        
        // Try all numbers from start to n
        for (let i = start; i <= n; i++) {
            current.push(i);
            backtrack(i + 1, current);
            current.pop();
        }
    }
    
    backtrack(1, []);
    return result;
};