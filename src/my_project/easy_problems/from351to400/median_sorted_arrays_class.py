from typing import List, Union
from abc import ABC, abstractmethod

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        solution = list()
        i = 0
        j = 0
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)

        while i < len_nums1 and j < len_nums2:

            if nums1[i] <= nums2[j]:
                solution.append(nums1[i])
                i += 1
            else: 
                solution.append(nums2[j])
                j += 1 
            
        solution = solution + nums1[i:] + nums2[j:]
        len_solution = len_nums1 + len_nums2
        return solution[len_solution//2] if len_solution%2 != 0 else (solution[len_solution//2 -1 ] + solution[len_solution//2])/2


class SolutionTwo:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        temp = nums1 + nums2
        temp.sort()

        print(temp)

        len_temp = len(temp)

        if len_temp % 2 == 0:
            return (temp[(len_temp//2)-1] + temp[len_temp//2])/2
        else: 
            return temp[len_temp//2]

