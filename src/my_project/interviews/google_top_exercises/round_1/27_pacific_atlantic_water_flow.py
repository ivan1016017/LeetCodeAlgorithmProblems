from typing import List
from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """Reverse DFS from each ocean's border, then intersect the two sets.

        Instead of asking "can this cell reach an ocean?" for every cell, we start
        at the ocean edges and walk uphill (neighbor height >= current height).
        Every cell reached that way can flow back down into that ocean.
        """

        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r: int, c: int, visited: set, prev_height: int):
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                    (r, c) in visited or heights[r][c] < prev_height):
                return

            visited.add((r, c))
            height = heights[r][c]

            dfs(r - 1, c, visited, height)
            dfs(r + 1, c, visited, height)
            dfs(r, c - 1, visited, height)
            dfs(r, c + 1, visited, height)

        # Top row -> Pacific, bottom row -> Atlantic
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])

        # Left column -> Pacific, right column -> Atlantic
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        return [[r, c] for r, c in pacific & atlantic]

    def pacificAtlantic_BFS(self, heights: List[List[int]]) -> List[List[int]]:
        """Same idea with multi-source BFS - avoids Python's recursion limit."""

        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])

        def bfs(starts: List[tuple]) -> set:
            visited = set(starts)
            q = deque(starts)

            while q:
                r, c = q.popleft()
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols and
                            (nr, nc) not in visited and
                            heights[nr][nc] >= heights[r][c]):
                        visited.add((nr, nc))
                        q.append((nr, nc))

            return visited

        pacific_starts = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        atlantic_starts = ([(rows - 1, c) for c in range(cols)] +
                           [(r, cols - 1) for r in range(rows)])

        return [[r, c] for r, c in bfs(pacific_starts) & bfs(atlantic_starts)]
