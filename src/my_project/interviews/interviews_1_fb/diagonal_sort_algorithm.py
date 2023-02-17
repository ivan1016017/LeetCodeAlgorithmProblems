from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import defaultdict


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        data = defaultdict(List)

        # place diagonal into dictionary
        for i, row in enumerate(mat):
            for j, num in enumerate(row):
                data[i-j].append(num)

        # sort diagonals
        for diag in data:
            data[diag].sort()

        # put back data into the matrix
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = data[i-j].pop(0)

        return mat

            