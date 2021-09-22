from typing import List 

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count: int = 0

        for item in operations:
            if item == "X++" or item == "++X":
                count += 1
            else:
                count -= 1

        return count 


solution = Solution()

print(solution.finalValueAfterOperations(operations = ["++X","++X","X++"]))