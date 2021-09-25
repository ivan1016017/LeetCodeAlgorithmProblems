from typing import List 

class Solution:
    def defangIPaddr(self, address: str) -> str:

        address = address.replace(".", "[.]")


        return address

solution = Solution()

print(solution.defangIPaddr(address = "1.1.1.1"))