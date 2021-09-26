from typing import List 

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count: int = 0
        for i in range(len(stones)):
            if stones[i] in jewels:
                count += 1
        return count 



solution = Solution()

print(solution.numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))