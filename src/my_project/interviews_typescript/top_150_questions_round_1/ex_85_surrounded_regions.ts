function solve(board: string[][]): void {
    /**
     * Do not return anything, modify board in-place instead.
     */
    if (!board || !board[0]) {
        return;
    }
    
    const m = board.length;
    const n = board[0].length;
    
    // BFS to mark all 'O's connected to border
    function bfs(row: number, col: number): void {
        const queue: [number, number][] = [[row, col]];
        board[row][col] = 'T';  // Temporary marker for safe 'O's
        
        while (queue.length > 0) {
            const [r, c] = queue.shift()!;
            // Check all 4 directions
            const directions: [number, number][] = [[0, 1], [0, -1], [1, 0], [-1, 0]];
            for (const [dr, dc] of directions) {
                const nr = r + dr;
                const nc = c + dc;
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && board[nr][nc] === 'O') {
                    board[nr][nc] = 'T';
                    queue.push([nr, nc]);
                }
            }
        }
    }
    
    // Step 1: Mark all border-connected 'O's
    // Check first and last row
    for (let col = 0; col < n; col++) {
        if (board[0][col] === 'O') {
            bfs(0, col);
        }
        if (board[m - 1][col] === 'O') {
            bfs(m - 1, col);
        }
    }
    
    // Check first and last column
    for (let row = 0; row < m; row++) {
        if (board[row][0] === 'O') {
            bfs(row, 0);
        }
        if (board[row][n - 1] === 'O') {
            bfs(row, n - 1);
        }
    }
    
    // Step 2: Flip all remaining 'O's to 'X' and restore 'T' back to 'O'
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (board[i][j] === 'O') {
                board[i][j] = 'X';  // Surrounded region
            } else if (board[i][j] === 'T') {
                board[i][j] = 'O';  // Border-connected, restore
            }
        }
    }
}