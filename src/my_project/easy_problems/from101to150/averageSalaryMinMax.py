from typing import List 

class Solution:
    def average(self, salary: List[int]) -> float:


        max_number: int = max(salary)
        min_number: int = min(salary)

        salary.sort()
        total_sum: int = 0

        for i in range(1, len(salary)-1,1):
            total_sum += salary[i]

        return total_sum/(len(salary)-2)


solution = Solution()

print(solution.average(salary = [4000,3000,1000,2000]))

print(solution.average(salary = [6000,5000,4000,3000,2000,1000]))

