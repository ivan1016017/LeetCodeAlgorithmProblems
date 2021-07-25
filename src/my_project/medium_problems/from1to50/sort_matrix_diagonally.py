from typing import List
from collections import defaultdict

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        data = defaultdict(list)

        # place diagonal into the dictionary
        for i, row in enumerate(mat):
            for j, num in enumerate(row):
                data[i-j].append(num)

        # sort the diagonals
        for diag in data:
            data[diag].sort()

        # put back into the matrix
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = data[i-j].pop(0)
        return mat

sample = defaultdict(list)

sample[3].append(10)
sample[3].append(20)
sample[8].append(2)
print(sample)

for i in sample:
    print(i)

my_list = [3,1,3,9,2]
print()
print(my_list.pop(0))
print(my_list.pop(0))
print(my_list.pop(0))
print(my_list)


