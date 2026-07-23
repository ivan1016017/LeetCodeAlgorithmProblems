from typing import Optional
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # HashMap to store original node -> cloned node mapping
        old_to_new = {}
        
        # BFS approach
        queue = deque([node])
        old_to_new[node] = Node(node.val)
        
        while queue:
            curr = queue.popleft()
            
            # Process all neighbors
            for neighbor in curr.neighbors:
                # If neighbor hasn't been cloned yet
                if neighbor not in old_to_new:
                    # Clone the neighbor
                    old_to_new[neighbor] = Node(neighbor.val)
                    # Add to queue for processing
                    queue.append(neighbor)
                
                # Add the cloned neighbor to the current cloned node's neighbors
                old_to_new[curr].neighbors.append(old_to_new[neighbor])
        
        return old_to_new[node]
    