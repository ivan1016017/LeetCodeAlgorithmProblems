from typing import List


class SecondSolution:
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

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        l1, l2 = len(firstList), len(secondList)
        res = []

        while i<l1 and j<l2:
            if secondList[j][0]>firstList[i][1]:
                i+=1
            elif secondList[j][1]<firstList[i][0]:
                j+=1
            elif secondList[j][0]>=firstList[i][0]:
                res.append([max(secondList[j][0], firstList[i][0]), min(secondList[j][1], firstList[i][1])])
                if j<l2-1 and secondList[j+1][0]<=firstList[i][1]:
                    j+=1
                else:
                    i+=1
            elif secondList[j][0]<=firstList[i][0]:
                res.append([max(secondList[j][0], firstList[i][0]), min(secondList[j][1], firstList[i][1])])
                if i<l1-1 and firstList[i+1][0]<=secondList[j][1]:
                    i+=1
                else:
                    j+=1
        return res


solution = Solution()
print(solution.intervalIntersection(firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]))