import collections
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0] or grid[0][0] == 1 or grid[-1][-1] == 1: return -1
        visited = set((0, 0))
        queue = collections.deque([(0, 0, 1)])
        
        while queue:
            x, y, level = queue.popleft()
            if (x, y) == (len(grid) - 1, len(grid[0]) - 1): return level
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x + dx][y + dy] == 0 and (x + dx, y + dy) not in visited:
                    visited.add((x + dx, y + dy))
                    queue.append((x + dx, y + dy, level + 1))
            
        return -1