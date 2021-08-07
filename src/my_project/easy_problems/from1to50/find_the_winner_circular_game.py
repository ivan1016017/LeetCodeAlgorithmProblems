from typing import List

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        # initialize variables
        len_n: int = n
        solution: List[int] = [x+1 for x in range(n)]
        count: int = 0

        while len_n > 1:

            count += k -1

            count = count % len_n

            solution.pop(count)

            len_n = len(solution)



        return solution[0]


solution = Solution()
print(solution.findTheWinner(5,2))