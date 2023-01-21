from typing import List, Union
from abc import ABC, abstractmethod

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num): return '0'
        num = [l for l in num]
        
        while k > 0:
            flag = True
            for i in range(len(num)-1):
                if str(num[i]) > str(num[i+1]):
                    num.pop(i)
                    k, flag = k - 1, False
                    break
                    
            if flag == True and num[i+1] == num[-1]: 
                num.pop(i+1)
                k -= 1
        
        return str(int(''.join(num)))

solution = Solution()

print(solution.removeKdigits(num = "10001", k = 4))



        
 