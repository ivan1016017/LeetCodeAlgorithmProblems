from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        candidates = ["()"]
        for i in range(1, n):
            new_candidates = set()
            for candidate in candidates:
                for j in range(0, len(candidate)):
                    next_candidate = candidate[:j] + "()" + candidate[j:]
                    new_candidates.add(next_candidate)
            candidates = list(new_candidates)
        return candidates

solution = Solution()


sample = "abc"
print(sample[:1])