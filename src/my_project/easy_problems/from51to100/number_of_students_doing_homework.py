from typing import List

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:

        # initialize variables
        len_times = len(startTime)
        count = 0

        for i in range(len_times):
            if queryTime >= startTime[i] and queryTime <= endTime[i]:
                count += 1

        return count


solution = Solution()
print(solution.busyStudent(startTime = [4], endTime = [4], queryTime = 5))