from typing import List 

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        out = []
        print(sorted(intervals, key=lambda i: i[0]))
        for i in sorted(intervals, key=lambda i: i[0]):
            if out and i[0] <= out[-1][-1]:
                out[-1][-1] = max(out[-1][-1], i[-1])
            else:
                out += i,
        return out
    
    
solution = Solution()

print(solution.merge([[2,6],[8,10],[1,3],[15,18]]))