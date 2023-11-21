from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def myPow(self, x, n):

        if not n: 
            return 1
        if n < 0: 
            return 1/self.myPow(x,-n)
        if n % 2: 
            return x*self.myPow(x,n-1)
        return self.myPow(x*x,n//2)