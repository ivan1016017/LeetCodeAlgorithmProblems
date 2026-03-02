function snakesAndLadders(board: number[][]): number {
    const n = board.length;
    
    // Helper function to convert square number to (row, col) coordinates
    function getPosition(square: number): [number, number] {
        // square is 1-indexed, convert to 0-indexed
        square -= 1;
        // Calculate row from bottom (0 is bottom row)
        const row = Math.floor(square / n);
        // Calculate column based on row direction
        let col: number;
        if (row % 2 === 0) {
            // Even rows (from bottom): left to right
            col = square % n;
        } else {
            // Odd rows (from bottom): right to left
            col = n - 1 - (square % n);
        }
        // Convert to board coordinates (0 is top row in board)
        return [n - 1 - row, col];
    }
    
    // BFS to find shortest path
    const target = n * n;
    const queue: [number, number][] = [[1, 0]]; // [current_square, num_moves]
    const visited = new Set<number>([1]);
    
    while (queue.length > 0) {
        const [curr, moves] = queue.shift()!;
        
        // Try all possible dice rolls (1 to 6)
        for (let dice = 1; dice <= 6; dice++) {
            let nextSquare = curr + dice;
            
            // Check if we've gone beyond the board
            if (nextSquare > target) {
                break;
            }
            
            // Get the board position for this square
            const [r, c] = getPosition(nextSquare);
            
            // Check if there's a snake or ladder
            if (board[r][c] !== -1) {
                nextSquare = board[r][c];
            }
            
            // Check if we've reached the target
            if (nextSquare === target) {
                return moves + 1;
            }
            
            // Add to queue if not visited
            if (!visited.has(nextSquare)) {
                visited.add(nextSquare);
                queue.push([nextSquare, moves + 1]);
            }
        }
    }
    
    // If we can't reach the target
    return -1;
}