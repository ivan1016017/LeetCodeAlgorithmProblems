from typing import List 

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        solution: List[int] = list()
        for item in ops:
            if item == "C":
                solution.pop()
                continue
            elif item == "D":
                solution.append(int(solution[-1])*2)
                continue
            elif item == "+":
                solution.append(int(solution[-1]) + int(solution[-2]))
                continue
            else:
                solution.append(int(item))


        return sum(solution )


solution = Solution()


print(solution.calPoints(ops = ["5","2","C","D","+"]))
print(solution.calPoints( ops = ["5","-2","4","C","D","9","+","+"]))