from typing import List
if __name__ == '__main__':

    class Solution:
        def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

            flag_row = True
            flag_col = None
            m = len(matrix)
            n = len(matrix[0])
            increase_row = 0
            increase_col = 1
            temp = list()
            temp_count = 0
            for i in range((m * n) - 1):

                if flag_row:
                    if increase_row % 2 == 0:
                        k = increase_row
                        temp.append(matrix[k][i + increase_row])
                    elif increase_row % 2 != 0:
                        k = (m - 1) - increase_row
                        temp.append(matrix[k][n-1-i])

                    if i - (n - 1 - increase_row) == 0:
                        flag_col = True
                        flag_row = False
                        increase_row += 1
                        continue

                if flag_col:
                    if increase_col % 2 == 0:
                        k = (n - 1) - increase_col
                        temp.append(matrix[i][k])
                    else:
                        k = increase_col
                        temp.append(matrix[i][k])

                    if i - (n - increase_col) == 0:
                        flag_col = False
                        flag_row = True
                        increase_col += 1
                        continue

            print("Hello")


    solution = Solution()
    solution.spiralOrder([1])
