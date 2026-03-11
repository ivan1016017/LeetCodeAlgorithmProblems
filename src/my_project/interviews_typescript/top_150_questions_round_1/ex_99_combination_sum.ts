function combinationSum(candidates: number[], target: number): number[][] {
    const result: number[][] = [];
    
    function backtrack(start: number, current: number[], remaining: number): void {
        // Base case: found a valid combination
        if (remaining === 0) {
            result.push([...current]);
            return;
        }
        
        // Base case: exceeded target
        if (remaining < 0) {
            return;
        }
        
        // Explore all candidates starting from 'start' index
        for (let i = start; i < candidates.length; i++) {
            // Include candidates[i] in the current combination
            current.push(candidates[i]);
            
            // Recurse with the same start index (we can reuse the same number)
            backtrack(i, current, remaining - candidates[i]);
            
            // Backtrack: remove the last added element
            current.pop();
        }
    }
    
    backtrack(0, [], target);
    return result;
}