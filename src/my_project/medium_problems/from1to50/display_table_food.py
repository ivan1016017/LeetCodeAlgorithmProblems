from typing import List
from collections import defaultdict

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:

        # initialize variables
        records = dict()
        menu_labels = set()
        solution = list()

        for order in orders:
            records[order[1]] = defaultdict(int)
            menu_labels.add(order[2])



        for order in orders:
            records[order[1]][order[2]] += 1


        sample_keys= list(records.keys())
        sample_keys = [int(x) for x in sample_keys]
        sample_keys.sort()


        solution = list()
        solution.append(["Table"])
        solution[0] += menu_labels

        for table in sample_keys:
            solution.append([str(table)])

            for name_dish in menu_labels:
                solution[-1].append(records[str(table)][name_dish])



        return solution


solution = Solution()
print(solution.displayTable(orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]))

