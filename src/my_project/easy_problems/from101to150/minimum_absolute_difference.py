from typing import List 
from math import inf 

class SecondSolution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        arr.sort()

        list_pairs = list()
        len_arr = len(arr)
        for i in range(len_arr):
            for j in range(i+1, len_arr):
                list_pairs.append([arr[i], arr[j]])

        list_pairs.sort(key= lambda x: abs(x[0]-x[1]))

        list_pairs = [x for x in list_pairs if abs(x[0] - x[1]) == abs(list_pairs[0][0] - list_pairs[0][1])]

        return list_pairs


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        answer = list()
        arr.sort()
        min_distance = inf 
        temp = 0

        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] <= min_distance:
                min_distance = arr[i+1] - arr[i]
                if temp > min_distance :
                    answer.clear()
                temp = min_distance
                answer.append([arr[i], arr[i+1]])
        


        return answer 


solution = Solution()

print(solution.minimumAbsDifference(arr = [4,2,1,3]))

print(solution.minimumAbsDifference(arr = [1,3,6,10,15]))


print(solution.minimumAbsDifference(arr = [3,8,-10,23,19,-4,-14,27]))



