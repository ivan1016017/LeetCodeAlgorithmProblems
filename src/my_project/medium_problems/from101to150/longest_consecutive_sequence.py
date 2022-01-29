from typing import List 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        h = set(nums)
        
        
        ans = 0
        while h:
            x = h.pop()
            count = 1
            
            a, b = x-1,x+1 
            
            while a in h:
                count +=1
                h.remove(a)
                a -= 1
                
            while b in h:
                count += 1
                h.remove(b)
                b += 1
            
            ans = max(ans, count)
        
        return ans