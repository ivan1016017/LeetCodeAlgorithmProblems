function generateParenthesis(n: number): string[] {
    const result: string[] = [];
    
    function backtrack(current: string, openCount: number, closeCount: number): void {
        // Base case: we've used all n pairs
        if (current.length === 2 * n) {
            result.push(current);
            return;
        }
        
        // Add opening parenthesis if we haven't used all n
        if (openCount < n) {
            backtrack(current + '(', openCount + 1, closeCount);
        }
        
        // Add closing parenthesis if it doesn't exceed opening count
        if (closeCount < openCount) {
            backtrack(current + ')', openCount, closeCount + 1);
        }
    }
    
    backtrack('', 0, 0);
    return result;
}