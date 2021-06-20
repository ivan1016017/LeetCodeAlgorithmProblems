

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        #initialize variables
        text1 = " " + text1
        text2 = " " + text2

        temp_count = 0


        len_text1 = len(text1)
        len_text2 = len(text2)

        matrix_c = [ [None for y in range(len_text2)] for x in range(len_text1) ]
        matrix_b = [ [None for y in range(len_text2)] for x in range(len_text1) ]


        for i in range(len_text1):
            matrix_c[i][0] = 0
        for j in range(len_text2):
            matrix_c[0][j] = 0

        for i in range(1,len_text1):
            for j in range(1,len_text2):
                if text1[i] == text2[j]:
                    matrix_c[i][j] = matrix_c[i-1][j-1] + 1
                    temp_count += 1
                    matrix_b[i][j] = "diagonal"
                elif matrix_c[i-1][j] > matrix_c[i][j-1]:
                    matrix_c[i][j] = matrix_c[i-1][j]
                    matrix_b[i][j] = "left"
                elif matrix_c[i - 1][j] <= matrix_c[i][j - 1]:
                    matrix_c[i][j] = matrix_c[i][j-1]
                    matrix_b[i][j] = "up"





        return matrix_c[-1][-1]

        # return temp_count

solution = Solution()

print(solution.longestCommonSubsequence("ezupkr", "ubmrapg"))