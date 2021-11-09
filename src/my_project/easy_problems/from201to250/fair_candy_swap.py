from typing import List 

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum1 = sum(aliceSizes)
        
        sum2 = sum(bobSizes)
        
        if sum1 > sum2:
            gap = (sum1 - sum2)//2
            for i in aliceSizes:
                if i-gap in bobSizes:
                    return [i,i-gap]
        else:
            gap = (sum2 - sum1)//2
            for i in bobSizes :
                if i-gap in aliceSizes:
                    return [i-gap,i]
                
solution = Solution()

print(solution.fairCandySwap(aliceSizes = [1,1], bobSizes = [2,2]))

print(solution.fairCandySwap(aliceSizes = [1,2], bobSizes = [2,3]))

print(solution.fairCandySwap(aliceSizes = [2], bobSizes = [1,3]))

print(solution.fairCandySwap(aliceSizes = [1,2,5], bobSizes = [2,4]))


