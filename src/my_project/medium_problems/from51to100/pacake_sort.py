from typing import List

class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        ans = []
        if len(arr) < 2:
            return []
        b = sorted(arr)
        arrayLen = len(arr)
        while arrayLen > 1:
            for i in range(arrayLen - 1):
                if arr[i] == arrayLen and i != arrayLen - 1:
                    ans.append(i + 1)
                    arr[0: i + 1] = arr[0: i+1][::-1]
                    arr[: arrayLen] = arr[:arrayLen][::-1]
                    ans.append(arrayLen)
                    break

            if b == arr:
                return ans
            arrayLen -= 1