from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic_answer = dict()

        for k, v in enumerate(nums):

            if v in dic_answer:
                return [dic_answer[v], k]
            else: 
                dic_answer[target - v] = k