from typing import List 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        negs = []
        poss = []
        num_of_zeros = 0
        
        for i in nums:
            if i == 0:
                num_of_zeros += 1
            elif i < 0:
                negs.append(i)
            else:
                poss.append(i)
        
        s_negs = set(negs)
        s_poss = set(poss)
        
        for i in range(len(poss)):
            for j in range(i+1, len(poss)):
                k = poss[i] + poss[j]
                if -k in s_negs:
                    mi = min(poss[i], poss[j])
                    ma = max(poss[i], poss[j])
                    result.append((-k, mi, ma))
                    
        for i in range(len(negs)):
            for j in range(i+1, len(negs)):
                k = negs[i] + negs[j]
                if -k in s_poss:
                    mi = min(negs[i], negs[j])
                    ma = max(negs[i], negs[j])
                    result.append((mi, ma, -k))
                    
        if num_of_zeros > 0:
            for i in s_poss:
                if -i in s_negs:
                    result.append((-i, 0, i))
                    
        if num_of_zeros > 2:
            result.append((0,0,0))
            
        return list(set(result))
        