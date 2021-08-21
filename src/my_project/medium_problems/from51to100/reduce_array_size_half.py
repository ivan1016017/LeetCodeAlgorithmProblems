from typing import List
from collections import defaultdict

class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        count_dict = defaultdict(int)
        half_len_arr = len(arr)//2

        for num in arr:
            count_dict[num] += 1


        list_counts = list(count_dict.values())
        list_counts.sort(reverse=True)

        count = 0
        for i, j in enumerate(list_counts):
            count += j
            if count >= half_len_arr:
                return i + 1


        return i + 1

solution = Solution()

print(solution.minSetSize(arr = [3,3,3,3,5,5,5,2,2,7]))

sample = [2,3,100,5]
sample.remove(max(sample))
print(sample)