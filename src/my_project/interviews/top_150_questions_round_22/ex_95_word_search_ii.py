from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import deque, defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Store the complete word at the end node

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build Trie from words
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word
        
        m, n = len(board), len(board[0])
        result = []
        
        def dfs(i, j, node):
            # Get current character
            char = board[i][j]
            
            # Check if character exists in Trie
            if char not in node.children:
                return
            
            next_node = node.children[char]
            
            # If we found a word, add it to result
            if next_node.word:
                result.append(next_node.word)
                next_node.word = None  # Avoid duplicate results
            
            # Mark cell as visited
            board[i][j] = '#'
            
            # Explore all 4 directions
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != '#':
                    dfs(ni, nj, next_node)
            
            # Restore cell
            board[i][j] = char
            
            # Optimization: remove leaf nodes to prune the Trie
            if not next_node.children:
                del node.children[char]
        
        # Start DFS from each cell
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
        
        return result
        