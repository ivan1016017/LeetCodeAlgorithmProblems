from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import deque, defaultdict

class WordDictionary:

    def __init__(self):
        self.root = {}
        

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['$'] = True  # Mark end of word
        

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return '$' in node
            
            char = word[i]
            if char == '.':
                # Wildcard: try all possible characters at this position
                for key in node:
                    if key != '$' and dfs(node[key], i + 1):
                        return True
                return False
            else:
                # Exact character match
                if char not in node:
                    return False
                return dfs(node[char], i + 1)
        
        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)