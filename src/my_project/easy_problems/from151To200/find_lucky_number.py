from typing import List 

class Solution:
    def findLucky(self, arr: List[int]) -> int:

        dict_solution = dict()
        list_solution = list()

        for item in arr:
            dict_solution[item] = 0



        for item in arr:
            dict_solution[item] += 1


        for i in dict_solution.keys():
            if dict_solution[i] == int(i):
                list_solution.append(i)

        if not list_solution:
            return -1

        
        return max(list_solution)


solution = Solution()

print(solution.findLucky(arr = [2,2,3,4]))

print(solution.findLucky(arr = [1,2,2,3,3,3]))

print(solution.findLucky(arr = [2,2,2,3,3]))

print(solution.findLucky(arr = [7,7,7,7,7,7,7]))

