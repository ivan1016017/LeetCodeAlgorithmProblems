from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        lst_s = [c for c in s]
        lst_t = [c for c in t]

        lst_s.sort()
        lst_t.sort()

        return lst_s == lst_t