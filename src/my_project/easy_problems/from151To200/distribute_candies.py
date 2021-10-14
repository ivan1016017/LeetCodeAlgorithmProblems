from typing import List 
from collections import Counter
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:

        count: int = 0
        list_distinct_candies: list[int] = list()

        for candy in candyType:
            if candy not in list_distinct_candies:
                list_distinct_candies.append(candy)
                count += 1

        if count <= len(candyType)//2:
            return count
        else:
            return len(candyType)//2

        
class SecondSolution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType) // 2, len(Counter(candyType)))

solution = Solution()

print(solution.distributeCandies(candyType = [1,1,2,2,3,3]))

print(solution.distributeCandies(candyType = [1,1,2,3]))

print(solution.distributeCandies(candyType = [6,6,6,6]))

