class Solution:
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        
        for i in range(1, n+1):
            if n % i == 0:
                k -= 1
                if k == 0:
                    return i 
        
        return -1

    

        
