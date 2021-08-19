from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        solution = list()
        for first_interval in firstList:
            for second_interval in secondList:
                if first_interval[1] < second_interval[0]:
                    break
                elif first_interval[0] > second_interval[1]:
                    continue
                else:
                    solution.append([max(first_interval[0], second_interval[0]), min(first_interval[1],second_interval[1])])


        return solution


solution = Solution()
print(solution.intervalIntersection(firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]))