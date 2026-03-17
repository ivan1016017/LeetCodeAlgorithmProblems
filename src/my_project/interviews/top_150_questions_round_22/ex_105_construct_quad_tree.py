from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import deque, defaultdict


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def is_all_same(r1: int, r2: int, c1: int, c2: int) -> tuple[bool, int]:
            """Check if all values in the subgrid are the same.
            Returns (True, value) if all same, (False, -1) otherwise.
            """
            val = grid[r1][c1]
            for i in range(r1, r2):
                for j in range(c1, c2):
                    if grid[i][j] != val:
                        return False, -1
            return True, val
        
        def build_tree(r1: int, r2: int, c1: int, c2: int) -> 'Node':
            """Build quad tree for subgrid from (r1,c1) to (r2,c2) exclusive."""
            all_same, val = is_all_same(r1, r2, c1, c2)
            
            if all_same:
                # Create leaf node
                return Node(val == 1, True, None, None, None, None)
            
            # Not all same, divide into 4 quadrants
            row_mid = (r1 + r2) // 2
            col_mid = (c1 + c2) // 2
            
            top_left = build_tree(r1, row_mid, c1, col_mid)
            top_right = build_tree(r1, row_mid, col_mid, c2)
            bottom_left = build_tree(row_mid, r2, c1, col_mid)
            bottom_right = build_tree(row_mid, r2, col_mid, c2)
            
            return Node(True, False, top_left, top_right, bottom_left, bottom_right)
        
        n = len(grid)
        return build_tree(0, n, 0, n)
        