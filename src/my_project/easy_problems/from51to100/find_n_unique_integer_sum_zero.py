from typing import List

class SecondSolution:
    def sumZero(self, n: int) -> List[int]:

        # initialize variables
        solution = list()
        n -= 1
        for i in range(n):
            solution.append(i+1)

        number = -n*(n+1)//2


        solution.append(number)


        return solution


class Solution:
    def sumZero(self, n: int) -> List[int]:



        # initialize variables
        solution = list()
        n -= 1
        number = 0
        for i in range(n):
            solution.append(i+1)
            number -= i + 1



        solution.append(number)


        return solution


solution = Solution()
print(solution.sumZero(5))