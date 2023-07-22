from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.dic = OrderedDict()


    def get(self, key: int) -> int:

        if key not in self.dic:
            return -1
        val = self.dic[key]
        self.dic.move_to_end(key)
        return val 

    def put(self, key: int, value: int) -> None:
        
        self.dic[key] = value  
        self.dic.move_to_end(key)

        if len(self.dic) > self.capacity:
            self.dic.popitem(last=False)


class LRUCacheTwo:

    def __init__(self, capacity):
        self.dict = {}
        self.cap = capacity

    def get(self, key) :
        if key not in self.dict : return -1
        k,v = key, self.dict[key]
        del self.dict[key]
        self.dict[k] = v
        return self.dict[key]

    def put(self, key, value) :
        if key not in self.dict:
            self.dict[key] = value
        else:
            k,v = key, self.dict[key]
            del self.dict[key]
            self.dict[key] = value
        if len(self.dict)>self.cap:
            del self.dict[list(self.dict.keys())[0]]