from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # initialize dict
        temp_dict:dict= dict()
        len_indices = len(indices)
        solution = ""

        for i in range(len_indices):
            temp_dict[indices[i]] = s[i]

        for i in range(len_indices):
            solution +=  temp_dict[i]

        return solution


solution = Solution()
print(solution.restoreString("codeleet", [4,5,6,7,0,2,1,3]))