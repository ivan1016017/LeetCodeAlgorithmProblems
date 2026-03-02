from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import deque, defaultdict

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        """
        Find minimum number of mutations from startGene to endGene.
        Uses BFS to find shortest path. Each mutation changes one character,
        and the resulting gene must be in the bank.
        
        Time Complexity: O(N * L * 4) where N is bank size, L is gene length (8)
        Space Complexity: O(N) for visited set and queue
        """
        # If endGene is not in bank, it's impossible
        if endGene not in bank:
            return -1
        
        # Convert bank to set for O(1) lookup
        bank_set = set(bank)
        
        # BFS queue: (current_gene, mutation_count)
        queue = deque([(startGene, 0)])
        visited = {startGene}
        
        # Possible gene characters
        genes = ['A', 'C', 'G', 'T']
        
        while queue:
            current_gene, mutations = queue.popleft()
            
            # If we reached the end gene, return the mutation count
            if current_gene == endGene:
                return mutations
            
            # Try all possible single character mutations
            for i in range(len(current_gene)):
                for gene_char in genes:
                    # Skip if same character
                    if gene_char == current_gene[i]:
                        continue
                    
                    # Create mutated gene
                    mutated = current_gene[:i] + gene_char + current_gene[i+1:]
                    
                    # If mutation is valid and not visited
                    if mutated in bank_set and mutated not in visited:
                        visited.add(mutated)
                        queue.append((mutated, mutations + 1))
        
        # No path found
        return -1