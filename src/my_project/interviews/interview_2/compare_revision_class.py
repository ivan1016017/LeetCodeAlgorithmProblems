from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        temp1 = version1.split('.')
        temp2 = version2.split('.')


        if len(temp1)> len(temp2):
            for i in range(len(temp1)-len(temp2)):
                temp2.append('0')
        if len(temp1) < len(temp2):
            for i in range(len(temp2)-len(temp1)):
                temp1.append('0')
        if len(temp1) == len(temp2):
            for i in range(len(temp1)):
                if int(temp1[i]) < int(temp2[i]):
                    return -1
                elif int(temp1[i]) > int(temp2[i]):
                    return 1
                else: 
                    continue 
            return 0

solution = Solution()


print(solution.compareVersion(version1 = "1.0", version2 = "1.0.0"))

        