/**
 * 52. N-Queens II
 * 
 * Given an integer n, return the number of distinct solutions to the n-queens puzzle.
 * 
 * The n-queens puzzle is placing n queens on an n×n chessboard such that
 * no two queens attack each other (same row, column, or diagonal).
 * 
 * Time Complexity: O(N!)
 * Space Complexity: O(N)
 */
function totalNQueens(n: number): number {
    // Track occupied columns, diagonals, and anti-diagonals
    const cols = new Set<number>();
    const diagonals = new Set<number>();  // row - col is constant for each diagonal
    const antiDiagonals = new Set<number>();  // row + col is constant for each anti-diagonal
    
    function backtrack(row: number): number {
        // Base case: all queens placed successfully
        if (row === n) {
            return 1;
        }
        
        let count = 0;
        // Try placing queen in each column of current row
        for (let col = 0; col < n; col++) {
            // Calculate diagonal and anti-diagonal identifiers
            const diagonal = row - col;
            const antiDiagonal = row + col;
            
            // Check if current position is safe
            if (cols.has(col) || diagonals.has(diagonal) || antiDiagonals.has(antiDiagonal)) {
                continue;
            }
            
            // Place queen
            cols.add(col);
            diagonals.add(diagonal);
            antiDiagonals.add(antiDiagonal);
            
            // Recurse to next row
            count += backtrack(row + 1);
            
            // Backtrack: remove queen
            cols.delete(col);
            diagonals.delete(diagonal);
            antiDiagonals.delete(antiDiagonal);
        }
        
        return count;
    }
    
    return backtrack(0);
}

export { totalNQueens };
