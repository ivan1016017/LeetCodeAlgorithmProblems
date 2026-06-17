from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import Counter

class Solution:
    def minimumKeypresses(self, s: str) -> int:
        """
        Greedy approach: Assign most frequent characters to 1-press slots
        
        Example: s = "apple"
        Frequency: {'p': 2, 'a': 1, 'l': 1, 'e': 1}
        
        Assignment:
        - 'p' (freq=2) → position 0 → 1 press → total: 2 * 1 = 2
        - 'a' (freq=1) → position 1 → 1 press → total: 1 * 1 = 1
        - 'l' (freq=1) → position 2 → 1 press → total: 1 * 1 = 1
        - 'e' (freq=1) → position 3 → 1 press → total: 1 * 1 = 1
        
        Total: 2 + 1 + 1 + 1 = 5
        """
        
        # Count character frequencies
        freq = Counter(s)
        print(freq)
        
        # Sort by frequency (descending) - greedy choice
        counts = sorted(freq.values(), reverse=True)
        print(counts)
        
        total_presses = 0
        
        # Calculate presses based on position
        for position, frequency in enumerate(counts):
            # Positions 0-8: 1 press (9 slots)
            # Positions 9-17: 2 presses (9 slots)
            # Positions 18-26: 3 presses (9 slots)
            presses_per_char = (position // 9) + 1
            total_presses += presses_per_char * frequency
        
        return total_presses        
            