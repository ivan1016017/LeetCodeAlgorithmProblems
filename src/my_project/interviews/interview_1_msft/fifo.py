from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class MyQueue:

    def __init__(self):
        self.temp_list: List[int] = list()
        

    def push(self, x: int) -> None:
        self.temp_list.append(x)
        

    def pop(self) -> int:
        temp = self.temp_list[0]
        self.temp_list = self.temp_list[1:]
        return temp
    
        

    def peek(self) -> int:
        return self.temp_list[0]
        

    def empty(self) -> bool:
        return not self.temp_list
        