from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.ans = []
        ds = []
        self.solve(0, s, ds)
        return self.ans

    def solve(self, idx, s, ds):
        if idx == len(s):
            self.ans.append(ds[:])
            return
        for i in range(idx, len(s)):
            if s[idx:i + 1] == s[idx:i + 1][::-1]:
                ds.append(s[idx:i + 1])
                self.solve(i + 1, s, ds)
                ds.pop()
        return


solution = Solution()
print(solution.partition("aab"))

print(solution.partition("abcdeff"))
