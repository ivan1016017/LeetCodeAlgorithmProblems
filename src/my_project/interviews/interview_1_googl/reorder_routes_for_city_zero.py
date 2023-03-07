from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import deque, defaultdict

class Solution:

    """
    Short description:

    In this solution, we add cities one by one to the country map. This addition follows 3 rules:

    1) If the first city of the road is already on the map, we need to change direction of this road and add a new city to the map.
    2) If the second city of the road is already on the map, we only add a new city to the map.
    3) If both cities are not on the map, we postpone this road and select next one.

    """
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        cmap = {0}
        count = 0
        dq = deque(connections)
        while dq:
            u, v = dq.popleft()
            if v in cmap:
                cmap.add(u)
            elif u in cmap:
                cmap.add(v)
                count += 1
            else:
                dq.append([u, v])
        return count
    
class SolutionTwo:
    def minReorderTwo(self, n, c):
        graph = defaultdict(list)
        conn = set()
        for i, j in c:
            graph[i].append(j)
            graph[j].append(i)
            conn.add((i, j))
        # print(graph)
        queue = deque([0])
        visited = {0}
        change = 0
        while queue:
            parent = queue.popleft()
            for child in graph[parent]:
                if child not in visited:
                    if (child, parent) not in conn:
                        # print(child, parent)
                        change += 1
                    queue.append(child)
                    visited.add(child)
        return change
            