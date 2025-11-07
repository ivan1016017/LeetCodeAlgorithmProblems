from typing import List, Union, Collection, Mapping, Optional
from collections import defaultdict

class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:

        groups = defaultdict(list)

        for num in nums:
            groups[num % k].append(num)

        res = 1

        for group in groups.values():
            group.sort()

            i = 0
            while i < len(group):
                chain = [group[i]]

                j = i + 1

                while j < len(group) and group[j] == chain[-1] + k:
                    chain.append(group[j])
                    j += 1

                m = len(chain)
                if m == 1:
                    chain_res = 2 # {} and {chain[0]}
                else:
                    take = 1
                    skip = 1

                    for i in range(1,m):
                        new_take = skip 
                        new_skip = take + skip
                        take, skip = new_take, new_skip

                    chain_res = take + skip 


                res *= chain_res

                i = j 

        return res
