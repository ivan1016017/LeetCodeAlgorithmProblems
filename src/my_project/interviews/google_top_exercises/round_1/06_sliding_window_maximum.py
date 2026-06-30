from typing import List
from collections import deque



class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Monotonic deque of indices, values in decreasing order.
        # Front always holds the index of the current window's max.
        answer = list()
        dq = deque()

        for i, num in enumerate(nums):
            # Drop indices whose values can never be the max again.
            while dq and nums[dq[-1]] <= num:
                dq.pop()
            dq.append(i)

            # Drop the front if it has slid out of the window.
            if dq[0] <= i - k:
                dq.popleft()

            # Start recording once the first full window is formed.
            if i >= k - 1:
                answer.append(nums[dq[0]])

        return answer    