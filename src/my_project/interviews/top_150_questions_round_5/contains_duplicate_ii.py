from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        answer_dic = defaultdict(int)
        len_num = len(nums)

        for i in range(len_num):

            answer_dic[nums[i]] += 1

            if i > k: 
                answer_dic[nums[i -(k+1)]] -= 1

            if answer_dic[nums[i]] > 1:
                return True 
            
        return False 