
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    pass

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        for i in range(1 , n +1):
            if isBadVersion(i):
                return i


class Solution2:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        h = n
        ans = 0

        while (h >= l):
            m = (l + h) // 2
            if isBadVersion(m):
                ans = m
                h = m - 1
            else:
                l = m + 1
        return ans