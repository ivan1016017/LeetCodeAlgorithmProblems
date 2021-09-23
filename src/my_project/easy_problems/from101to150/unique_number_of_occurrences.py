from typing import List
from collections import defaultdict, OrderedDict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        order_dict = defaultdict(int)

        for i in arr:
            order_dict[i] += 1


        solution_set = set()

        solution: List[int] = list()

        for i in order_dict.values():
            solution.append(i)

        solution_set = set(solution)

        return len(solution) == len(solution_set)

solution = Solution()

print(solution.uniqueOccurrences(arr = [1,2,2,1,1,3]))

