from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:


        count = 0
        flag = False

        for item in words:
            flag = False
            for i in set(item):
                if i not in allowed:
                    flag = True
                    break
            if flag:
                continue
            else:
                count += 1

        return count

solution = Solution()
print(solution.countConsistentStrings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"]))
print(solution.countConsistentStrings(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]))
print(solution.countConsistentStrings(allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]))
