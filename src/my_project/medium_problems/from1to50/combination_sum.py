from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(remain, comb, start):
            if remain == 0:
                result.append(list(comb))
                return
            for i in range(start, len(candidates)):
                if remain - candidates[i] < 0:  # optimization, skip the rest elements becuase they are larger than candidates[i]  (candidates is sorted)
                    break
                backtrack(remain - candidates[i], comb + [candidates[i]], i)  # [] convert candidates[i] to a list

        backtrack(target, [], 0)
        return result








solution = Solution()
print(solution.combinationSum([2,3,2,6,7], 7))

print(8//2)

for i in range(8//2):
    print(i)

