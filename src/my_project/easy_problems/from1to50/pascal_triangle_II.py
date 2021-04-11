from typing import List

if __name__ == '__main__':
    class Solution:
        def getRow(self, rowIndex: int) -> List[int]:
            temp = list()
            rowIndex += 1
            if rowIndex == 1:
                return [[1]][-1]
            elif rowIndex == 2:
                return [[1], [1, 1]][-1]
            elif rowIndex >= 3:

                list_pascal = [1, 1]
                i = 3
                while i <= rowIndex:

                    for j in range(i):
                        if j == 0:
                            temp.append(list_pascal[0])
                        if j == (i - 1):
                            temp.append(list_pascal[-1])
                        elif j > 0 and j < i - 1:
                            temp.append(list_pascal[j - 1] + list_pascal[j])

                    i += 1
                    list_pascal = temp
                    temp = list()
                return list_pascal

    solution = Solution()
    print(solution.getRow(1))