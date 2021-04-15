import math

class Solution:
    def reverseBits(self, n: int) -> int:
        temp_binary = self.from_decimal_to_binary(n)
        temp_binary = temp_binary[::-1]
        temp_decimal = self.from_binary_to_decimal(temp_binary)
        return temp_decimal


    def from_decimal_to_binary(self,n:int) -> str:

        quotient = math.inf
        temp_binary = str()
        while quotient >0:
            quotient, remainder = n // 2, n %2
            temp_binary = str(remainder) + temp_binary
            n = quotient

        return temp_binary

    def from_binary_to_decimal(self,binary_number: str) -> int:
        temp = 0
        len_binary = len(binary_number)
        for i in range(len_binary):
            temp = temp + int(binary_number[len_binary -1 - i])* (2**i)
        return temp

solution = Solution()
print(solution.reverseBits(11))
sample = "abc"
print(sample[::-1])