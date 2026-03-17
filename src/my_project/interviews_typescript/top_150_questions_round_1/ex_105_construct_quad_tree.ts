class _Node {
    val: boolean
    isLeaf: boolean
    topLeft: _Node | null
    topRight: _Node | null
    bottomLeft: _Node | null
    bottomRight: _Node | null
    constructor(val?: boolean, isLeaf?: boolean, topLeft?: _Node | null, topRight?: _Node | null, bottomLeft?: _Node | null, bottomRight?: _Node | null) {
        this.val = (val===undefined ? false : val)
        this.isLeaf = (isLeaf===undefined ? false : isLeaf)
        this.topLeft = (topLeft===undefined ? null : topLeft)
        this.topRight = (topRight===undefined ? null : topRight)
        this.bottomLeft = (bottomLeft===undefined ? null : bottomLeft)
        this.bottomRight = (bottomRight===undefined ? null : bottomRight)
    }
}

function construct(grid: number[][]): _Node | null {
    /**
     * Check if all values in the subgrid are the same.
     * Returns [true, value] if all same, [false, -1] otherwise.
     */
    function isAllSame(r1: number, r2: number, c1: number, c2: number): [boolean, number] {
        const val = grid[r1][c1];
        for (let i = r1; i < r2; i++) {
            for (let j = c1; j < c2; j++) {
                if (grid[i][j] !== val) {
                    return [false, -1];
                }
            }
        }
        return [true, val];
    }
    
    /**
     * Build quad tree for subgrid from (r1,c1) to (r2,c2) exclusive.
     */
    function buildTree(r1: number, r2: number, c1: number, c2: number): _Node {
        const [allSame, val] = isAllSame(r1, r2, c1, c2);
        
        if (allSame) {
            // Create leaf node
            return new _Node(val === 1, true, null, null, null, null);
        }
        
        // Not all same, divide into 4 quadrants
        const rowMid = Math.floor((r1 + r2) / 2);
        const colMid = Math.floor((c1 + c2) / 2);
        
        const topLeft = buildTree(r1, rowMid, c1, colMid);
        const topRight = buildTree(r1, rowMid, colMid, c2);
        const bottomLeft = buildTree(rowMid, r2, c1, colMid);
        const bottomRight = buildTree(rowMid, r2, colMid, c2);
        
        return new _Node(true, false, topLeft, topRight, bottomLeft, bottomRight);
    }
    
    const n = grid.length;
    return buildTree(0, n, 0, n);
}