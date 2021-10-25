from typing import List 

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def _max_value(data: List[int]) -> int:
            return data.pop(data.index(max(data)))
            
        while len(stones) > 1:
            value = abs(_max_value(stones) - _max_value(stones))
            if value:
                stones.append(value)
        return stones[0] if stones else 0


solution = Solution()

print(solution.lastStoneWeight(stones = [2,7,4,1,8,1]))

print(solution.lastStoneWeight(stones = [1]))
