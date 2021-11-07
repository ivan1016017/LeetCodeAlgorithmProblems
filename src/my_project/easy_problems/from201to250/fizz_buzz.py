from typing import List 

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        solution = [str(i+1) for i in range(n)]
        for i in range(n):
            if (i+1)% 3 == 0 and (i+1)%5 == 0:
                solution[i] = "FizzBuzz"
            elif (i+1) % 3 == 0:
                solution[i] = "Fizz"
            elif (i+1) % 5 == 0:
                solution[i] = "Buzz"

        return solution 

solution = Solution()

print(solution.fizzBuzz(n = 3))

print(solution.fizzBuzz(n = 5))

print(solution.fizzBuzz( n = 15))
