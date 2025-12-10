from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        Performs text justification by distributing words and spaces across lines of fixed width.
        
        Strategy: Build lines word by word until adding the next word would exceed maxWidth.
        When a line is full, distribute extra spaces evenly using round-robin.
        """
        result = []           # Final list of justified lines
        current_list = []     # Words being accumulated for the current line
        num_of_letters = 0    # Total character count (excluding spaces) in current_list
        
        for word in words:
            # Check if adding this word exceeds the line width
            # Formula: letters + new_word_length + minimum_spaces_needed
            # Minimum spaces = one space between each word = len(current_list)
            if num_of_letters + len(word) + len(current_list) > maxWidth:
                # Justify and add the current line to results
                
                # Calculate number of gaps between words (n words = n-1 gaps)
                # Use max(1, ...) to handle single-word lines and avoid division by zero
                num_gaps = max(1, len(current_list) - 1)
                
                # Distribute extra spaces using round-robin
                # Total spaces needed = maxWidth - num_of_letters
                extra_spaces = maxWidth - num_of_letters
                for i in range(extra_spaces):
                    # Use modulo to cycle through gaps repeatedly
                    # This ensures spaces are distributed as evenly as possible
                    gap_index = i % num_gaps
                    current_list[gap_index] += ' '
                
                # Join words into a single justified line and add to result
                result.append("".join(current_list))
                
                # Reset for next line
                current_list = []
                num_of_letters = 0
            
            # Add current word to the line being built
            current_list.append(word)
            num_of_letters += len(word)
        
        # form last line by join with space and left justify to maxWidth using ljust (python method)
        # that means pad additional spaces to the right to make string length equal to maxWidth
        result.append(" ".join(current_list).ljust(maxWidth))
        
        return result