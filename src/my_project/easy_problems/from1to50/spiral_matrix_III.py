from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        i ,j = rStart, cStart
        inc = 1
        ans = [[rStart, cStart]]
        while len(ans) < rows*cols:
            if inc % 2 == 0:
                c = inc * -1
            else:
                c = inc
            z = abs(c)
            while z > 0:
                if c < 0:
                    j -= 1
                else:
                    j += 1
                if i in range(0, rows) and j in range(0, cols):
                    ans.append([i, j])
                z -= 1
            z = abs(c)
            while z > 0:
                if c < 0:
                    i -= 1
                else:
                    i += 1
                if i in range(0, rows) and j in range(0, cols):
                    ans.append([i, j])
                z -= 1
            inc += 1
        return ans