from typing import List 

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        origin_list: List[str] = list()
        destination_list: List[str] = list()

        for city in paths:
            origin_list.append(city[0])

        
        for city in paths:
            if city[1] not in origin_list:
                destination_list.append(city[1])

        return destination_list[0]

solution = Solution()

print(solution.destCity(paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))

print(solution.destCity(paths = [["B","C"],["D","B"],["C","A"]]))

print(solution.destCity(paths = [["A","Z"]]))

