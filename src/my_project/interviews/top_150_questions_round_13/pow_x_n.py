from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def myPow(self, x, n):

        if not n: 
            return 1 
        elif n < 0:
            return self.myPow(1/x, -n)
        elif n % 2: 
            return x*self.myPow(x,n-1)
        else:
            return self.myPow(x*x, n//2)