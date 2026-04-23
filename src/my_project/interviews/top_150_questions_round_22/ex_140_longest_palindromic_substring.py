class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, max_len = 0, 1

        def expand(left: int, right: int) -> None:
            nonlocal start, max_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            length = right - left - 1
            if length > max_len:
                max_len = length
                start = left + 1

        for i in range(len(s)):
            expand(i, i)      # odd-length
            expand(i, i + 1)  # even-length

        return s[start:start + max_len]
