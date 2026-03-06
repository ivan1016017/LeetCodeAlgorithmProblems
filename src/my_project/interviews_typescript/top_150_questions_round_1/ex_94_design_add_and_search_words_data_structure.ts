class WordDictionary {
    private root: Map<string, any>;

    constructor() {
        this.root = new Map();
    }

    addWord(word: string): void {
        let node = this.root;
        for (const char of word) {
            if (!node.has(char)) {
                node.set(char, new Map());
            }
            node = node.get(char);
        }
        node.set('$', true);  // Mark end of word
    }

    search(word: string): boolean {
        const dfs = (node: Map<string, any>, i: number): boolean => {
            if (i === word.length) {
                return node.has('$');
            }
            
            const char = word[i];
            if (char === '.') {
                // Wildcard: try all possible characters at this position
                for (const [key, childNode] of node.entries()) {
                    if (key !== '$' && dfs(childNode, i + 1)) {
                        return true;
                    }
                }
                return false;
            } else {
                // Exact character match
                if (!node.has(char)) {
                    return false;
                }
                return dfs(node.get(char), i + 1);
            }
        };
        
        return dfs(this.root, 0);
    }
}