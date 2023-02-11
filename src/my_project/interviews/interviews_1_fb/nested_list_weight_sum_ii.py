from typing import List, Collection, Mapping, Optional, Union
from abc import ABC, abstractmethod

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution:
    def _sum(self, nestedList,dep):
        int_sum = 0
        lst_sum = 0
        
        for x in nestedList:
            if x.isInteger():
                int_sum += x.getInteger()
            else:
                lst_sum += self._sum(x.getList(),dep-1)
                
        return int_sum * dep + lst_sum
    
    def _get_depth(self,nestedList):
        if nestedList == []:
            return 0
        depth = 1
        for x in nestedList:
            if not x.isInteger():
                depth = max(depth, self._get_depth(x.getList())+1)
        return depth
    
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        rt_depth = self._get_depth(nestedList)
        return self._sum(nestedList, rt_depth)