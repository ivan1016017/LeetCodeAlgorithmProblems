class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        Count trailing zeroes in n! by counting factors of 5.
        
        Key insight: Trailing zeroes come from 10 = 2 * 5.
        Since there are always more factors of 2 than 5 in n!,
        we just need to count factors of 5.
        
        We count: floor(n/5) + floor(n/25) + floor(n/125) + ...
        This counts all multiples of 5, 25, 125, etc.
        
        Time complexity: O(log n) - we divide by 5 each iteration
        Space complexity: O(1)
        """
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count