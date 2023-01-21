from typing import List, Union
from abc import ABC, abstractmethod

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        key idea is remove those digit which is larger than its right digit,
        :type num: str
        :type k: int
        :rtype: str
        """

        i, n = 0, len(num)
        res = []
        count = 0
        while i < n - 1 and count < k:
            # if num[i]> num[i+1] , num[i] is one need to be removed,so don't add it to res
            # and we check the res from tail, pop those larger than num[i+1]
            if num[i] > num[i + 1]:
                count += 1
                while len(res) > 0 and res[-1] > num[i + 1] and count < k:
                    res.pop()
                    count += 1
            else:
                res.append(num[i])
            i += 1
        res = "".join(res)
        # if does not remove enough, we have remove count digit, still need to remove k-count digit,
        #  currently, the res is in ascending order, we need to remove k-count-1 digit from tail of res
        if count < k:
            res = (res[:len(res) - (k - count - 1)]).lstrip('0')
        else:
            # if we have removed k digits, add the remaining of num to res
            res = (res + num[i:]).lstrip('0')
        return res if len(res) > 0 else "0"

solution = Solution()

print(solution.removeKdigits(num = "10001", k = 4))



        
 