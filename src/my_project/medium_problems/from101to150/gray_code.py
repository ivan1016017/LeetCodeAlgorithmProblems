from typing import List 

'''
Awesome! Why does X = Y & -Y give us the lowest bit? Here is an explanation:

~Y inverts all bits. Also
~Y = -Y - 1 (widely used - hello Python's negative list indexes).
-Y = ~Y + 1 This will give us an idea of what -Y looks like in bin

0000000000000101 = Y
1111111111111010 = ~Y
1111111111111011 = ~Y + 1 = -Y

0000000000000001 = Y & -Y

'''

class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, 2**n):
            res.append(res[-1] ^ (i & -i))
        return res
        