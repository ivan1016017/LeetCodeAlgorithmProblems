import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k

        def quickselect(left: int, right: int) -> int:
            pivot_index = random.randint(left, right)
            pivot = nums[pivot_index]

            # 3-way partition (Dutch National Flag)
            low = left
            mid = left
            high = right

            while mid <= high:
                if nums[mid] < pivot:
                    nums[low], nums[mid] = nums[mid], nums[low]
                    low += 1
                    mid += 1
                elif nums[mid] > pivot:
                    nums[mid], nums[high] = nums[high], nums[mid]
                    high -= 1
                else:
                    mid += 1

            # All elements equal to pivot are in [low, high]
            if target < low:
                return quickselect(left, low - 1)
            elif target > high:
                return quickselect(high + 1, right)
            else:
                return nums[target]

        return quickselect(0, len(nums) - 1)
