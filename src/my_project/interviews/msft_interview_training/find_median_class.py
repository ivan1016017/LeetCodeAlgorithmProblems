from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
import heapq

class MedianFinder:

    def __init__(self):
        self.lst = list()
        

    def addNum(self, num: int) -> None:
        if not self.lst: 
            self.lst.append(num)
            return 
        l = 0
        r = len(self.lst) -1 
        while l < r: 
            m = (l+r)//2
            if self.lst[m] == num:
                self.lst.insert(m,num)
                return 
            elif self.lst[m] < num:
                l = m + 1
            else: 
                r = m -1
        if self.lst[l] < num: 
            self.lst.insert(l+1,num)
        else: 
            self.lst.insert(l,num)
        

    def findMedian(self) -> float:

        temp = sorted(self.lst)
        len_tmp = len(temp)
        if len_tmp % 2 == 1: 
            return temp[len_tmp//2]
        else: 
            return (temp[len_tmp//2] + temp[(len_tmp//2) - 1])/2
        

class MedianFinderTwo:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.small = [] # store the small half, top is the largest in the small part
        self.large = [] # store the large half, top is the smallest in the large part

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if len(self.small) == 0:
            heapq.heappush(self.small, -num)
            return
        if num <= -self.small[0]:
            # push to small part
            heapq.heappush(self.small, -num)
        else:
            # push to large part
            heapq.heappush(self.large, num)
        # adjust small and large balance
        if len(self.small) - len(self.large) == 2:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.small) - len(self.large) == -2:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0])/2.0
        return -float(self.small[0]) if len(self.small) > len(self.large) else float(self.large[0])
    
    
        
