from typing import List 

class Solution:

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        rooms = 0

        if not intervals:
            return rooms 
        
        count_end = 0
        
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)

        for i in range(len(intervals)):

            if starts[i] >= ends[count_end]:
                count_end += 1
            else: 
                rooms += 1
        
        return rooms

    
solution = Solution()

print(solution.minMeetingRooms(intervals=[[0,10], [1,2], [3,4], [5,6]]))

