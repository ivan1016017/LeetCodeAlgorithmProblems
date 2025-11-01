from typing import List, Union, Collection, Mapping, Optional


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        k = sum(data) # window size 
        ans = val = 0 
        for i, x in enumerate(data): 
            val += x
            if i >= k: val -= data[i-k]
            if i+1 >= k: ans = max(ans, val)
        return k - ans
    
'''
Window size (k): Count total number of 1s in the array. This is the size of the window needed to fit all 1s.

Sliding window: Move a window of size k across the array and count how many 1s are already in each window position.

Find maximum 1s: Track the maximum number of 1s found in any window (ans).

Calculate swaps: The minimum swaps needed = k - ans (total 1s minus the maximum 1s already grouped in any window).
'''    
