from typing import List, Union 
from abc import ABC, abstractmethod

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        for i in range(len(image)):
            
            image[i].reverse()

        for i in range(len(image)):
            for j in range(len(image[0])):

                image[i][j] = 1 - image[i][j]

        return image 
        
