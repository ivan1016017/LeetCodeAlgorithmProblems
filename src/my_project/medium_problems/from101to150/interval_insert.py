from typing import List 


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        res = []
        for i in sorted(intervals, key=lambda x:x[0]):
            if res and res[-1][-1] >= i[0]:
               
                res[-1][-1] = max(res[-1][-1], i[-1])
            else:
                res.append(i)
        return res
        
solution = Solution()

print(solution.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))