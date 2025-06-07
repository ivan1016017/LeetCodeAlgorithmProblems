from typing import List

class Solution:

    def algo_1(self, names: List[str]):

        dic_solution = dict()

        for n in names:
            if n in dic_solution:
                dic_solution[n] += 1
            else: 
                dic_solution[n] = 1

        names.sort(key=lambda x: dic_solution[x], reverse=True)
        

        return names[0], dic_solution[names[0]]
    


solution = Solution()

print(solution.algo_1(names=['paola','mariana','mariana']))