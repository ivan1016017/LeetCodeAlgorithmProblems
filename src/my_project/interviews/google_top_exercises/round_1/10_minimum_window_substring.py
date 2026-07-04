from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        need = Counter(t)          # chars (with counts) still required
        missing = len(t)           # total chars still to satisfy
        left = 0
        best_left, best_len = 0, float("inf")

        for right, char in enumerate(s):
            # This char helps only if we still need it (count > 0)
            if need[char] > 0:
                missing -= 1
            need[char] -= 1

            # Window covers all of t: try to shrink from the left
            while missing == 0:
                if right - left + 1 < best_len:
                    best_left, best_len = left, right - left + 1

                need[s[left]] += 1
                # Dropping this char breaks coverage only if it was required
                if need[s[left]] > 0:
                    missing += 1
                left += 1

        return "" if best_len == float("inf") else s[best_left:best_left + best_len]