from typing import List, Union, Optional, Collection, Mapping
from abc import ABC, abstractmethod

class CustomStack:

    def __init__(self, maxSize: int):
        self.n = maxSize
        self.stack = list()
        

    def push(self, x: int) -> None:
        if len(self.stack) < self.n:
            self.stack.append(x)
        

    def pop(self) -> int:
        if not self.stack: return -1
        if len(self.stack) >= 1:
            temp = self.stack.pop()
            return temp

        

    def increment(self, k: int, val: int) -> None:

        for k in range(min(k,len(self.stack))):
            self.stack[k] += val 