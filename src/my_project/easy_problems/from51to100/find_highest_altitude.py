from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        count = 0
        temp = 0
        len_gain = len(gain)

        for i in range(0,len_gain):
            count += gain[i]
            if count > temp:
                temp = count
        return temp



solution = Solution()
print(solution.largestAltitude(gain = [-4,-3,-2,-1,4,3,2]))