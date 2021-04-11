from typing import List


if __name__ == '__main__':
    class Solution:
        def longestPalindrome(self, s: str) -> str:
            max_length = 0
            max_string = ""
            for i in range(len(s)):
                for j in range(i, len(s)):
                    temp = 1
                    for k in range(0, (j-i)):
                        if s[j-k] != s[i+k]:
                            temp = 0
                    if temp ==1 and (j-i) + 1 > max_length:
                        max_length = (j-i) + 1
                        max_string = "".join([x for x in s[i:(j+1)]])
            print(max_string)
            return max_length

    solution = Solution()
    print(solution.longestPalindrome("babad"))
