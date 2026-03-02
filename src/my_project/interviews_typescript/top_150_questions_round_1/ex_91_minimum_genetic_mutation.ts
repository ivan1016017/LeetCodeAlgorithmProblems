/**
 * 433. Minimum Genetic Mutation
 * 
 * A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.
 * Find the minimum number of mutations needed to mutate from startGene to endGene.
 * Each mutation changes one single character, and the resulting gene must be in the bank.
 * 
 * Time Complexity: O(N * L * 4) where N is bank size, L is gene length (8)
 * Space Complexity: O(N) for visited set and queue
 */

function minMutation(startGene: string, endGene: string, bank: string[]): number {
    // If endGene is not in bank, it's impossible
    if (!bank.includes(endGene)) {
        return -1;
    }
    
    // Convert bank to set for O(1) lookup
    const bankSet = new Set(bank);
    
    // BFS queue: [current_gene, mutation_count]
    const queue: [string, number][] = [[startGene, 0]];
    const visited = new Set<string>([startGene]);
    
    // Possible gene characters
    const genes = ['A', 'C', 'G', 'T'];
    
    while (queue.length > 0) {
        const [currentGene, mutations] = queue.shift()!;
        
        // If we reached the end gene, return the mutation count
        if (currentGene === endGene) {
            return mutations;
        }
        
        // Try all possible single character mutations
        for (let i = 0; i < currentGene.length; i++) {
            for (const geneChar of genes) {
                // Skip if same character
                if (geneChar === currentGene[i]) {
                    continue;
                }
                
                // Create mutated gene
                const mutated = currentGene.substring(0, i) + geneChar + currentGene.substring(i + 1);
                
                // If mutation is valid and not visited
                if (bankSet.has(mutated) && !visited.has(mutated)) {
                    visited.add(mutated);
                    queue.push([mutated, mutations + 1]);
                }
            }
        }
    }
    
    // No path found
    return -1;
}