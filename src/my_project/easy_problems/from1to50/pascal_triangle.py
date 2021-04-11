from typing import List

if __name__ == '__main__':
    class Solution:
        def generate(self, numRows: int) -> List[List[int]]:
            temp = list()
            list_rows = [[1],[1,1]]

            if numRows == 1:
                return [[1]]
            elif numRows == 2:
                return [[1], [1,1]]
            elif numRows >= 3:

                list_pascal = [1,1]
                i = 3
                while i <= numRows:

                    for j in range(i):
                        if j ==0:
                            temp.append(list_pascal[0])
                        if j == (i -1):
                            temp.append(list_pascal[-1])
                        elif j > 0 and j < i-1:
                            temp.append(list_pascal[j-1] + list_pascal[j])

                    i +=1
                    list_pascal = temp
                    list_rows.append(list_pascal)
                    temp = list()
                return list_rows


    solution = Solution()
    print(solution.generate(1))
    sample = [1,2,3]
    print(sample[-1])
    temp = sample
    sample = list()
    print(temp)
