from typing import List, Union, Collection, Mapping, Optional


class Solution:
    def minSwaps(self, data: List[int]) -> int:

        # Set window size
        k = sum(data)

        val = answer = 0

        for i, v in enumerate(data):

            val += v

            if i >= k:
                val -= data[i - k]

            if i >= k - 1:
                answer = max(answer, val)

        return k - answer
        
'''
Window size (k): Count total number of 1s in the array. This is the size of the window needed to fit all 1s.

Sliding window: Move a window of size k across the array and count how many 1s are already in each window position.

Find maximum 1s: Track the maximum number of 1s found in any window (ans).

Calculate swaps: The minimum swaps needed = k - ans (total 1s minus the maximum 1s already grouped in any window).
'''    
