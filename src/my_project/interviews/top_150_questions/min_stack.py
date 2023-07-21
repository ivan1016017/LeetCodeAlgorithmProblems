from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class MinStack:

    def __init__(self):
        self.temp_list = list()
        

    def push(self, val: int) -> None:
        self.temp_list.append(val)
        

    def pop(self) -> None:
        self.temp_list.pop()
        

    def top(self) -> int:
        return self.temp_list[-1]
        

    def getMin(self) -> int:
        return min(self.temp_list)
    
class MinStackTwo:
    def __init__(self):
        self.A = []
        self.M = []
    def push(self, x):
        self.A.append(x)
        self.M.append( x if not self.M else min(x, self.M[-1]) )
    def pop(self):
        self.A.pop()
        self.M.pop()
    def top(self):
        return self.A[-1]
    def getMin(self):
        return self.M[-1]