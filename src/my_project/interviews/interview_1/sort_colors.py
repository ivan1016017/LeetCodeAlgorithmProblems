from typing import List, Union 
from abc import ABC, abstractmethod

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        c0=c1=c2=0
        for num in nums: 
            if num==0:
                c0+=1
            elif num==1:
                c1+=1
            elif num==2:
                c2+=1

        nums[0:c0] = [0]*c0
        nums[c0:c0+c1] = [1]*c1 
        nums[c0+c1:c0+c1+c2] = [2]*c2 

        return nums
        

        pass 