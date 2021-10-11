from typing import List 

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:



        return (ord(coordinates[0]) + ord(coordinates[1]))%2 != 0


solution = Solution()

print(solution.squareIsWhite(coordinates = "a1"))

print(solution.squareIsWhite(coordinates = "h3"))

print(solution.squareIsWhite(coordinates = "c7"))
