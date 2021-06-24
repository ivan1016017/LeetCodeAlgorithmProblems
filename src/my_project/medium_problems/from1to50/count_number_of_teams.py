from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:

        # initialize variables
        len_rating = len(rating)
        dp = [[0 for y in range(len_rating)] for x in range(len_rating)]

        count = 0

        for i in range(len_rating):
            for j in range(i+1,len_rating):

                if rating[j] > rating[i]:
                    dp[j][0] += 1

                    count += dp[i][0]

                if rating[i]> rating[j]:
                    dp[j][1] += 1
                    count += dp[i][1]



        return count



solution = Solution()
print(solution.numTeams([2,5,3,4,1]))