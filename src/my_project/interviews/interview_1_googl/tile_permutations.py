from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from itertools import permutations
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        answer = 0
        len_tiles = len(tiles)
        for i in range(1,len_tiles+1):
            answer += len(set(permutations(tiles,i)))

        return answer 

solution = Solution()
print(solution.numTilePossibilities('AAB'))