from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
import math

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1[m:m+n] = nums2

        nums1.sort()


class SolutionTwo:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # initialize the index of nums1 and nums 2

        # assign the values of nums1 and nums2 to right_list and left_list
        left_list = list()
        right_list = list()
        for i in range(len(nums1) - len(nums2)):
            left_list.append(nums1[i])

        for i in range(len(nums2)):
            right_list.append(nums2[i])

        left_list.append(math.inf)
        right_list.append(math.inf)
        # index nums 1
        i = 0
        # index nums 2
        j = 0
        for l in range(len(nums1)):
            if left_list[i] < right_list[j]:
                nums1[l] = left_list[i]
                i += 1
            elif left_list[i] >= right_list[j]:
                nums1[l] = right_list[j]
                j += 1