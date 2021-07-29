from typing import List
from collections import defaultdict

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:


        data = defaultdict(set)
        uam = dict()
        inverted_uam = {k:0 for k in range(1,k+1)}
        solution = list()



        for item in logs:
            data[item[0]].add(item[1])

        for item in data:
            uam[item] = len(data[item])

        for key, values in uam.items():
            inverted_uam[values] +=1

        for values in inverted_uam.values():
            solution.append(values)


        return solution


solution = Solution()

print(solution.findingUsersActiveMinutes(logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5))

print(solution.findingUsersActiveMinutes(logs = [[1,1],[2,2],[2,3]], k = 4))