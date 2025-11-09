from typing import List, Union, Collection, Mapping, Optional

class Solution:
    def minSwaps(self, data: List[int]) -> int:

        # Window size 
        k = sum(data)

        answer = val = 0

        for i, v in enumerate(data):

            val += v 

            if i >= k: 
                val -= data[i - k]

            if i >= k - 1:
                answer = max(answer, val)

        return k - answer