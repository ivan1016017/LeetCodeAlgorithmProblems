from typing import List 

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        count_dict = dict()
        len_arr: int = len(arr)
        count: int = 0
        for i in range(len_arr):
            count_dict[arr[i]] = 0

        for i in range(len_arr):
            count_dict[arr[i]] += 1

        for i in count_dict.keys():
            if count_dict[i] == 1:
                count += 1
                if count == k:
                    return i 
        
        return "" 


solution = Solution()

print(solution.kthDistinct(arr = ["d","b","c","b","c","a"], k = 2))

print(solution.kthDistinct(arr = ["aaa","aa","a"], k = 1))

print(solution.kthDistinct(arr = ["a","b","a"], k = 3))
