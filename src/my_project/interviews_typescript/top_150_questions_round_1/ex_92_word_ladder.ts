function ladderLength(beginWord: string, endWord: string, wordList: string[]): number {
    /**
     * Find the shortest transformation sequence from beginWord to endWord.
     * Uses BFS to find the shortest path.
     * 
     * Time Complexity: O(M^2 * N) where M is word length, N is wordList size
     * Space Complexity: O(M^2 * N) for the pattern dictionary
     */
    
    // If beginWord equals endWord, the sequence is just the word itself
    if (beginWord === endWord) {
        return 1;
    }
    
    // If endWord is not in wordList, no valid transformation exists
    if (!wordList.includes(endWord)) {
        return 0;
    }
    
    // Convert wordList to set for O(1) lookup
    const wordSet = new Set<string>(wordList);
    
    // Add beginWord to the set if not present
    if (!wordSet.has(beginWord)) {
        wordSet.add(beginWord);
    }
    
    // Build a pattern dictionary to find all words that differ by one letter
    // e.g., "hot" -> {"*ot": ["hot"], "h*t": ["hot"], "ho*": ["hot"]}
    const patternDict = new Map<string, string[]>();
    const wordLen = beginWord.length;
    
    // Create patterns for all words
    for (const word of wordSet) {
        for (let i = 0; i < wordLen; i++) {
            const pattern = word.slice(0, i) + '*' + word.slice(i + 1);
            if (!patternDict.has(pattern)) {
                patternDict.set(pattern, []);
            }
            patternDict.get(pattern)!.push(word);
        }
    }
    
    // BFS to find shortest path
    const queue: [string, number][] = [[beginWord, 1]]; // [current_word, level]
    const visited = new Set<string>([beginWord]);
    
    while (queue.length > 0) {
        const [currentWord, level] = queue.shift()!;
        
        // Try all possible transformations by replacing each character
        for (let i = 0; i < wordLen; i++) {
            const pattern = currentWord.slice(0, i) + '*' + currentWord.slice(i + 1);
            
            // Get all words matching this pattern
            const neighbors = patternDict.get(pattern) || [];
            for (const nextWord of neighbors) {
                if (nextWord === endWord) {
                    return level + 1;
                }
                
                if (!visited.has(nextWord)) {
                    visited.add(nextWord);
                    queue.push([nextWord, level + 1]);
                }
            }
            
            // Clear the pattern to avoid revisiting in future iterations
            patternDict.set(pattern, []);
        }
    }
    
    return 0;
}

