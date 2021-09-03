from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:


        solution: int = 0

        arranged_boxTypes: List[List[int]] = list()

        while len(boxTypes) > 0:
            arranged_boxTypes.append(boxTypes.pop(self.indexMax(boxTypes)))


        for i in range(len(arranged_boxTypes)):
            if arranged_boxTypes[i][0] <= truckSize:
                solution += arranged_boxTypes[i][0] * arranged_boxTypes[i][1]
                truckSize -= arranged_boxTypes[i][0]
            elif  arranged_boxTypes[i][0] > truckSize:
                solution += truckSize*arranged_boxTypes[i][1]
                return solution
        return solution



    def indexMax(self, boxTypes: List[List[int]]) -> int:

        max: int  = -1
        index: int = None

        for i in range(len(boxTypes)):
            if boxTypes[i][1] > max:
                index = i
                max = boxTypes[i][1]

        return index

solution = Solution()



print(solution.maximumUnits(boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4))

print(solution.maximumUnits(boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10))




