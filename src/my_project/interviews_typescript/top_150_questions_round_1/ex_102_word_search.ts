function exist(board: string[][], word: string): boolean {
    if (!board || board.length === 0 || !board[0] || board[0].length === 0 || !word) {
        return false;
    }
    
    const rows = board.length;
    const cols = board[0].length;
    
    function dfs(row: number, col: number, index: number): boolean {
        // Base case: found all characters
        if (index === word.length) {
            return true;
        }
        
        // Check boundaries and character match
        if (row < 0 || row >= rows || 
            col < 0 || col >= cols || 
            board[row][col] !== word[index]) {
            return false;
        }
        
        // Mark cell as visited by temporarily changing it
        const temp = board[row][col];
        board[row][col] = '#';
        
        // Explore all 4 directions
        const found = dfs(row + 1, col, index + 1) ||
                     dfs(row - 1, col, index + 1) ||
                     dfs(row, col + 1, index + 1) ||
                     dfs(row, col - 1, index + 1);
        
        // Backtrack: restore the cell
        board[row][col] = temp;
        
        return found;
    }
    
    // Try starting from each cell
    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            if (dfs(row, col, 0)) {
                return true;
            }
        }
    }
    
    return false;
}