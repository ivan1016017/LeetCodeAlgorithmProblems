class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 0:
            return ''
        
        n = len(s)
        dp = [[False for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = True
        ans = s[0:1]
        for i in range(n):
            for j in range(i-1, -1, -1):
                if s[i] == s[j] and (i-j<2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if i - j + 1 > len(ans):
                        ans = s[j:i+1]
        return ans