from typing import List

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:

        # initialize variables
        len_queries = len(queries)
        permutation = [x+1 for x in range(m)]
        solution: List[int] = list()
        temp_index: int = None
        temp_value: int = None

        for i in range(len_queries):
            temp_index = self.simple_scann(permutation, queries[i])
            print(permutation)
            solution.append(temp_index)
            print(solution)
            temp_value = permutation.pop(temp_index)
            permutation = [temp_value] + permutation
        return solution

    def simple_scann(self, nums: List[int], target: int) -> List[int]:
        solution: int = None
        for i in range(len(nums)):
            if nums[i] == target:
                solution = i
        return solution


solution = Solution()

print(solution.simple_scann([7,5,5,8,3],  8))
print(solution.processQueries([7,5,5,8,3], m = 8))