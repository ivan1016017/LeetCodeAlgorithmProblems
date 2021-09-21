from typing import List 
from collections import Counter


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        c = Counter(nums)

        cc = sorted(nums, key=lambda l: (c[l],-l))



        return cc



class SecondSolution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        l = [(k,v) for k,v in count.items()]
        l.sort(key = lambda x:x[0], reverse=True)
        l.sort(key = lambda x:x[1])
        result = []
        for i in l:
            result.extend([i[0]]*i[1])
        return result

solution = Solution()

print(solution.frequencySort(nums = [1,1,2,2,2,3]))
