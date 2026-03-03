from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Find the shortest transformation sequence from beginWord to endWord.
        Uses BFS to find the shortest path.
        
        Time Complexity: O(M^2 * N) where M is word length, N is wordList size
        Space Complexity: O(M^2 * N) for the pattern dictionary
        """
        # If beginWord equals endWord, the sequence is just the word itself
        if beginWord == endWord:
            return 1
        
        # If endWord is not in wordList, no valid transformation exists
        if endWord not in wordList:
            return 0
        
        # Convert wordList to set for O(1) lookup
        word_set = set(wordList)
        
        # Build a pattern dictionary to find all words that differ by one letter
        # e.g., "hot" -> {"*ot": ["hot"], "h*t": ["hot"], "ho*": ["hot"]}
        pattern_dict = defaultdict(list)
        word_len = len(beginWord)
        
        # Add beginWord to the set if not present
        if beginWord not in word_set:
            word_set.add(beginWord)
        
        # Create patterns for all words
        for word in word_set:
            for i in range(word_len):
                pattern = word[:i] + '*' + word[i+1:]
                pattern_dict[pattern].append(word)
        
        # BFS to find shortest path
        queue = deque([(beginWord, 1)])  # (current_word, level)
        visited = {beginWord}
        
        while queue:
            current_word, level = queue.popleft()
            
            # Try all possible transformations by replacing each character
            for i in range(word_len):
                pattern = current_word[:i] + '*' + current_word[i+1:]
                
                # Get all words matching this pattern
                for next_word in pattern_dict[pattern]:
                    if next_word == endWord:
                        return level + 1
                    
                    if next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, level + 1))
                
                # Clear the pattern to avoid revisiting in future iterations
                pattern_dict[pattern] = []
        
        return 0