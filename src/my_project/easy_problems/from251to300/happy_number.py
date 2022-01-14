class Solution:
    def isHappy(self, n: int) -> bool:
        
        def get_next(n):
            total_sum = 0
            while n > 0:
                digit = n  % 10
                n = n // 10
                total_sum += digit ** 2
            return total_sum

        seen = list()
        while n != 1 and n not in seen:
            seen.append(n)
            n = get_next(n)

        return n == 1
        
        