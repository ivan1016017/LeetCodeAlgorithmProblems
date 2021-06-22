class Solution:
    def countVowelStrings(self, n: int) -> int:
        # initialize variables

        temp = [[0 for y in range(n+1) ] for x in range(5) ]


        temp[0][1] = temp[1][1] = temp[2][1] = temp[3][1] = temp[4][1] =1

        for i in range(2, n+1):
            temp[0][i] = temp[0][i-1] + temp[1][i-1] + temp[2][i-1] + temp[3][i-1] + temp[4][i-1]
            temp[1][i] = temp[1][i-1] + temp[2][i-1] + temp[3][i-1] + temp[4][i-1]
            temp[2][i] = temp[2][i - 1] + temp[3][i - 1] + temp[4][i - 1]
            temp[3][i] = temp[3][i - 1] + temp[4][i - 1]
            temp[4][i] = temp[4][i - 1]



        return temp[0][n] + temp[1][n] + temp[2][n] + temp[3][n] + temp[4][n]

solution = Solution()
print(solution.countVowelStrings(2))