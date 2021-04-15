class Solution:
    def hammingWeight(self, n: int) -> int:

        return len( [value for value in bin(n) if value == '1'])


solution = Solution()

print(bin(13))

