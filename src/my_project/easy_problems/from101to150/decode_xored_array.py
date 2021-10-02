from typing import List 

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        output = []
        output.append(first)
        n = len(encoded)
        for i in range(n):
            xor = output[i] ^ encoded[i]
            print(output[i], encoded[i],xor)
            output.append(xor)
        return output


solution = Solution()

print(solution.decode(encoded = [1,2,3], first = 1))

print(solution.decode( encoded = [6,2,7,3], first = 4))

a = bin(4)
b = bin(6)
print(a)
print(b)
print(bin(2))



