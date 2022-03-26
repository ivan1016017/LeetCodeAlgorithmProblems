from typing import List 

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        if(n == 0):
            return 0
        elif(n==1 or n == 2):
            return 1
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        count = 2
        check = 1
        number = 1
        while count <= n:
            if(check == 1 and count <= n):
                dp[(number*2)] = dp[number]
                check += 1
                count += 1
            if(check == 2 and count <= n):
                dp[(number*2)+1] = dp[number] + dp[number + 1]
                check = 1
                number += 1
                count += 1
            else:
                count += 1
        return max(dp)
        
        
        