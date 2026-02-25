from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import deque, defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Build graph: adjacency list with weights
        graph = defaultdict(dict)
        
        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1.0 / value
        
        def bfs(start: str, end: str) -> float:
            # Check if variables exist in graph
            if start not in graph or end not in graph:
                return -1.0
            
            # If start equals end and it exists in graph
            if start == end:
                return 1.0
            
            # BFS to find path from start to end
            queue = deque([(start, 1.0)])  # (node, accumulated_product)
            visited = {start}
            
            while queue:
                node, product = queue.popleft()
                
                # Check all neighbors
                for neighbor, weight in graph[node].items():
                    if neighbor == end:
                        return product * weight
                    
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, product * weight))
            
            return -1.0
        
        # Process all queries
        results = []
        for dividend, divisor in queries:
            results.append(bfs(dividend, divisor))
        
        return results