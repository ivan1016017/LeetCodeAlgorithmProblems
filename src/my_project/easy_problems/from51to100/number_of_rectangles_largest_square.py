from typing import List

class SecondSolution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:

        temp_list = list()
        count = 0
        for item in rectangles:
            temp_list.append(min(item[0],item[1]))

        max_number = max(temp_list)

        for item in temp_list:
            if item == max_number:
                count += 1
        return count




class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:

        temp_list = list()
        count = 0
        max = 0
        for item in rectangles:
            if min(item[0],item[1]) > max:
                max = min(item[0], item[1])
                count = 1
            elif min(item[0],item[1]) == max:
                count += 1
            else:
                continue

        return count

solution = Solution()
print(solution.countGoodRectangles(rectangles = [[2,3],[3,7],[4,3],[3,7]]))