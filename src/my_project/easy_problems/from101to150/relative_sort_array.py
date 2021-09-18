from typing import List 
import collections

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:


        arr = collections.Counter([x for x in arr1 if x in arr2])
        remaining = [x for x in arr1 if x not in arr2]
        # print(remaining)
        remaining.sort()
        
        # result=[]

        # print([item for item in arr2 for i in range(arr[item])] )
        
        return [item for item in arr2 for i in range(arr[item])]  + remaining


solution = Solution()

print(solution.relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]))