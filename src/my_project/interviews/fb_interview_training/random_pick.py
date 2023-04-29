from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
import random

class Solution:

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.cum_weights = [0]*len(w)
        summ = 0
        for i in range(len(w)):
            summ += w[i]
            self.cum_weights[i] = summ
        self.W = summ
        
    def bSearch(self, num):
        i = 0
        j = len(self.cum_weights)
        while i < j:
            mid = (i+j) // 2
            if num == self.cum_weights[mid]:
                return mid
            elif num > self.cum_weights[mid]:
                i = mid+1
            else:
                j = mid
        return i

    def pickIndex(self):
        """
        :rtype: int
        """
        num = random.randint(1, self.W)
        idx = self.bSearch(num)
        return idx
    

class SolutionTwo:
    def __init__(self, w: List[int]):
        self.w = w
		# 1. calculate relative frequency
        denom = sum(self.w)
        for i in range(len(self.w)):
            self.w[i] = self.w[i] / denom
        # 2. put relative frequencies on the number line between 0 and 1
		# Note self.w[-1] = 1
        for i in range(1,len(self.w)):
            self.w[i] += self.w[i-1]
        
    def pickIndex(self) -> int:
		
		# this is where we pick the index
        N = random.uniform(0,1)
      
        flag = 1
        index = -1
        
		# test each region of the numberline to see if N falls in it, if it 
		# does not then go to the next index and check if N falls in it
		# this is gaurenteed to break because of previous normalization
        while flag:
            index +=1 
           
           
     
            if N <= self.w[index]:
                flag = 0
        
    
        return index
    

