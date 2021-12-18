from typing import List 

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        if rounds[0] == rounds[-1]:
            return [rounds[0]]
        
        
        solution: List[int] = []
        
        if rounds[0] < rounds[-1]:
            for i in range(rounds[0], rounds[-1]+1):
                solution.append(i)
                
        else: 
            for i in range(rounds[0], rounds[-1] + 1 + n):
                if i == n:
                    solution.append(i)
                else:
                    solution.append(i%n)
        return sorted(solution)