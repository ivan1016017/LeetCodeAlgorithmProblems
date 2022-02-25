from typing import List 

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        n = 4
        v1 = [int(v) for v in version1.split('.')]
        v2 = [int(v) for v in version2.split('.')]
        while len(v1) < n:
            v1.append(0)
        while len(v2) < n:
            v2.append(0)
        for i in range(n):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
        return 0
        
