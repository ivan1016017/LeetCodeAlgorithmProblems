class TrieNode {
    children: Map<string, TrieNode>;
    word: string | null;

    constructor() {
        this.children = new Map();
        this.word = null; // Store the complete word at the end node
    }
}

function findWords(board: string[][], words: string[]): string[] {
    // Build Trie from words
    const root = new TrieNode();
    for (const word of words) {
        let node = root;
        for (const char of word) {
            if (!node.children.has(char)) {
                node.children.set(char, new TrieNode());
            }
            node = node.children.get(char)!;
        }
        node.word = word;
    }

    const m = board.length;
    const n = board[0].length;
    const result: string[] = [];

    function dfs(i: number, j: number, node: TrieNode): void {
        // Get current character
        const char = board[i][j];

        // Check if character exists in Trie
        if (!node.children.has(char)) {
            return;
        }

        const nextNode = node.children.get(char)!;

        // If we found a word, add it to result
        if (nextNode.word !== null) {
            result.push(nextNode.word);
            nextNode.word = null; // Avoid duplicate results
        }

        // Mark cell as visited
        board[i][j] = '#';

        // Explore all 4 directions
        const directions = [[0, 1], [1, 0], [0, -1], [-1, 0]];
        for (const [di, dj] of directions) {
            const ni = i + di;
            const nj = j + dj;
            if (ni >= 0 && ni < m && nj >= 0 && nj < n && board[ni][nj] !== '#') {
                dfs(ni, nj, nextNode);
            }
        }

        // Restore cell
        board[i][j] = char;

        // Optimization: remove leaf nodes to prune the Trie
        if (nextNode.children.size === 0) {
            node.children.delete(char);
        }
    }

    // Start DFS from each cell
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            dfs(i, j, root);
        }
    }

    return result;
}

  