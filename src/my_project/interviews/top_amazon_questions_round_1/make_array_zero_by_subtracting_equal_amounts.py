from typing import List 


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        answer = set([n for n in nums if n > 0])

        return len(answer)