

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp_dict_one = dict()
        temp_dict_two = dict()

        if len(s) != len(t):
            return False

        len_s = len(s)
        for i in  range(len_s):
            temp_dict_one[s[i]] = s.count(s[i])
            temp_dict_two[t[i]] = t.count(t[i])

        if temp_dict_one == temp_dict_two:
            return True

        else:
            return False


solution = Solution()
print(solution.isAnagram("anagram",  "nkgaram"))
