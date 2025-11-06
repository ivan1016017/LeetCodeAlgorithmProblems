from typing import List, Union, Collection, Mapping, Optional
from collections import defaultdict

class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        """
        Count k-Free subsets using dynamic programming.
        
        Approach:
        1. Group elements by (num % k) to find independent groups
        2. Within each group, sort and build chains where elements differ by k
        3. For each chain, use House Robber DP to count valid subsets
        4. Multiply results across all independent chains
        
        Time: O(n log n), Space: O(n)
        """
        # Group numbers by their remainder when divided by k
        groups = defaultdict(list)
        for num in nums:
            groups[num % k].append(num)
        
        res = 1
        
        # Process each group independently
        for group in groups.values():
            group.sort()
            
            # Build chains within this group
            i = 0
            while i < len(group):
                chain = [group[i]]
                j = i + 1
                
                # Build chain where each element is exactly k more than previous
                while j < len(group) and group[j] == chain[-1] + k:
                    chain.append(group[j])
                    j += 1
                
                # House Robber DP for this chain
                m = len(chain)
                if m == 1:
                    chain_res = 2  # {} or {chain[0]}
                else:
                    take = 1  # Take first element
                    skip = 1  # Skip first element
                    
                    for idx in range(1, m):
                        new_take = skip  # Can only take current if we skipped previous
                        new_skip = take + skip  # Can skip current regardless
                        take, skip = new_take, new_skip
                    
                    chain_res = take + skip
                
                res *= chain_res
                i = j
        
        return res