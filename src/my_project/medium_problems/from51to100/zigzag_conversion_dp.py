from typing import List 

class Solution:
    def convert(self, s: str, numRows: int) -> str:
    
           
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1
        
        print(L)

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step
            print(L)

        return ''.join(L)
    
    
solution = Solution()

print(solution.convert( s = "PAYPALISHIRING", numRows = 3))