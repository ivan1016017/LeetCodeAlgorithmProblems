import math
from typing import List

if __name__ == '__main__':
    class Solution:
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
                print(i,j)
                if left_list[i] < right_list[j]:
                    nums1[l] = left_list[i]
                    i += 1
                elif left_list[i] >= right_list[j]:
                    nums1[l] = right_list[j]
                    j += 1


    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solution = Solution()
    solution.merge(nums1,m,nums2,n)
    print(nums1)