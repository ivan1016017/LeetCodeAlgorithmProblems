class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        start = 0
        max_len = 1

        def expand(left: int, right: int) -> None:
            nonlocal start, max_len
            # Expand outward while the substring stays a palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Loop exits one step too far, so the palindrome is s[left+1 : right]
            length = right - left - 1
            if length > max_len:
                max_len = length
                start = left + 1

        for i in range(len(s)):
            expand(i, i)      # odd-length center
            expand(i, i + 1)  # even-length center

        return s[start:start + max_len]