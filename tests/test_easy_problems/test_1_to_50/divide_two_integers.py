import math

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        signal_dividend = self.signal(dividend)
        signal_divisor = self.signal(divisor)
        dividend = abs(dividend)
        divisor = abs(divisor)

        temp = 0
        result = 0
        if divisor > dividend:
            return 0
        else:

            while temp <= dividend:
                temp += divisor
                if temp <= dividend:
                    result += 1
                else:
                    break
            return (result * signal_dividend * signal_divisor)

    def signal(self, number: int) -> int:
        if number <= 0:
            return 1
        else:
            return -1


class SecondSolution:
    def div(self, dividend, divisor, sum, n):
        # core function
        if (sum << 1) > dividend and sum + divisor > dividend:
            return n
        if (sum << 1) > dividend:
            return n + self.div(dividend-sum, divisor, divisor , 1)
        else:
            return self.div(dividend, divisor, sum << 1, n + n)

    def divide(self, dividend: int, divisor: int) -> int:
        # special cases
        MAX = 2147483647
        if dividend == 0:
            return 0
        if abs(divisor) == 1:
            if  (dividend < 0 and divisor < 0):
                return min(MAX,abs(dividend))
            elif divisor < 0:
                return -dividend
            else:
                return dividend
        if abs(divisor) > abs(dividend):
            return 0

        # core begins
        if (dividend < 0 or divisor < 0) and not (dividend < 0 and divisor < 0):
            return -self.div(abs(dividend), abs(divisor), abs(divisor), 1)
        else:
            return self.div(abs(dividend), abs(divisor), abs(divisor), 1 )

solution = Solution()
print(solution.divide(10,3))
print(13 >> 1)
