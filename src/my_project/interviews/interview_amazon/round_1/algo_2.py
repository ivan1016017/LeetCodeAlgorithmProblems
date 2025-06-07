from typing import List

class Solution:

    def algo_1(self, names: List[str]):

        
        names.sort(key=lambda x: len(x), reverse=True)
        

        return names[0]
    


solution = Solution()

print(solution.algo_1(names=['paola','mariana','stephanos']))