from typing import List 
from collections import deque, defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        

        #
        n = len(isConnected)
        # construct an adjacency list
        adj = defaultdict(set)
        node_set = set()
        # 
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    node_set.add(i)
                    node_set.add(j)
                    if i != j:
                        adj[i].add(j)
                        adj[j].add(i)
        #
        visited = set()
        out = 0
        # 
        def bfs(node):
            _queue = deque()
            _queue.append(node)
            while _queue:
                curr_node = _queue.popleft()
                for temp_node in adj[curr_node]:
                    if temp_node not in visited:
                        _queue.append(temp_node)
                        visited.add(temp_node)
        #
        for temp_node in node_set:
            if temp_node in visited:
                pass
            else:
                # start a BFS from temp_node
                bfs(temp_node)
                out += 1
        #
        return(out)
        
        