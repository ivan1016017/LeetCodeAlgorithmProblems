from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        len_nums = len(nums)

        if len_nums == 0: return []
        if len_nums == 1: return [f'{nums[0]}']
        
        answer = list()
        pre = start = nums[0]

        for i in nums[1:]:

            if i - pre != 1:
                answer.append(f'{start}->{pre}' if pre-start>0 else f'{pre}')
                start = i 

            pre = i 

        answer.append(f'{start}->{pre}' if pre-start>0 else f'{pre}')

        return answer 
    
class SolutionTwo: 

    def summaryRanges(self, nums):
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:
                ranges += [],
            ranges[-1][1:] = n,
        return ['->'.join(map(str, r)) for r in ranges]