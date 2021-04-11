from typing import List

if __name__ == '__main__':
    class Solution:
        def addBinary(self, a: str, b: str) -> str:

            # take the length of the two stings
            len_a = len(a)
            len_b = len(b)
            # expand the strings (with zeros) to make them have the same size
            if len_a < len_b:
                temp_a = "0" * (len_b - len_a)
                a = temp_a + a
            if len_a > len_b:
                temp_b = "0" * (len_a - len_b)
                b = temp_b + b

            decimal_number = self.fromBinaryToDecimal(a) + self.fromBinaryToDecimal(b)
            binary_number = self.fromDecimalToBinary(decimal_number)
            return binary_number

        def fromBinaryToDecimal(self, binary_number: str) -> int:
            temp = 0
            len_binary = len(binary_number)
            for i in range(len(binary_number)):
                temp = temp + int(binary_number[len_binary - 1 - i]) * (2 ** (i))
            return temp

        def fromDecimalToBinary(self, decimal_number: str) -> str:

            quotient = 10 * 6
            remainder = 0
            temp = ""
            while quotient > 0:
                quotient, remainder = decimal_number // 2, decimal_number % 2
                temp = str(remainder) + temp
                decimal_number = quotient
            return temp


    solution = Solution()
    print(solution.addBinary("11", "1"))
    print("1".zfill(3))
    print(int("2") * 2)
    print(solution.fromBinaryToDecimal("1010"))
    print(solution.fromDecimalToBinary(13))

    print("ad" * 3)
