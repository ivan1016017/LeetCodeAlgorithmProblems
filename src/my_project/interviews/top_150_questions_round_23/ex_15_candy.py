from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        Distribute candies to children based on ratings.
        
        Rules:
        1. Each child gets at least 1 candy
        2. Children with higher rating than neighbors get more candies
        
        Strategy: Two-pass greedy
        - Left-to-right: Ensure each child has more candies than left neighbor if rating is higher
        - Right-to-left: Ensure each child has more candies than right neighbor if rating is higher
        - Take maximum from both passes to satisfy both neighbors
        
        Time: O(n), Space: O(n)
        """
        
        n = len(ratings)
        if n == 0:
            return 0
        
        # Initialize all children with 1 candy
        candies = [1] * n
        
        # Left-to-right pass: Compare with left neighbor
        # If current child has higher rating than left neighbor,
        # give them one more candy than left neighbor
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Right-to-left pass: Compare with right neighbor
        # If current child has higher rating than right neighbor,
        # ensure they have more candies (take max of current and right+1)
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        # Return total candies needed        
        return sum(candies)
    

"""
Example walkthrough for ratings = [1, 0, 2]:

Initial: candies = [1, 1, 1]

Left-to-right pass:
i=1: ratings[1]=0 < ratings[0]=1 → no change → candies = [1, 1, 1]
i=2: ratings[2]=2 > ratings[1]=0 → candies[2] = candies[1] + 1 = 2 → candies = [1, 1, 2]

Right-to-left pass:
i=1: ratings[1]=0 < ratings[2]=2 → no change → candies = [1, 1, 2]
i=0: ratings[0]=1 > ratings[1]=0 → candies[0] = max(1, 1+1) = 2 → candies = [2, 1, 2]

Total: 2 + 1 + 2 = 5


Example walkthrough for ratings = [1, 2, 2]:

Initial: candies = [1, 1, 1]

Left-to-right pass:
i=1: ratings[1]=2 > ratings[0]=1 → candies[1] = 1 + 1 = 2 → candies = [1, 2, 1]
i=2: ratings[2]=2 = ratings[1]=2 → no change → candies = [1, 2, 1]

Right-to-left pass:
i=1: ratings[1]=2 = ratings[2]=2 → no change → candies = [1, 2, 1]
i=0: ratings[0]=1 < ratings[1]=2 → no change → candies = [1, 2, 1]

Total: 1 + 2 + 1 = 4


Example walkthrough for ratings = [1, 3, 2, 2, 1]:

Initial: candies = [1, 1, 1, 1, 1]

Left-to-right:
i=1: 3 > 1 → candies[1] = 2 → [1, 2, 1, 1, 1]
i=2: 2 < 3 → no change → [1, 2, 1, 1, 1]
i=3: 2 = 2 → no change → [1, 2, 1, 1, 1]
i=4: 1 < 2 → no change → [1, 2, 1, 1, 1]

Right-to-left:
i=3: 2 > 1 → candies[3] = max(1, 2) = 2 → [1, 2, 1, 2, 1]
i=2: 2 = 2 → no change → [1, 2, 1, 2, 1]
i=1: 3 > 2 → candies[1] = max(2, 2) = 2 → [1, 2, 1, 2, 1]
i=0: 1 < 3 → no change → [1, 2, 1, 2, 1]

Total: 1 + 2 + 1 + 2 + 1 = 7
"""
