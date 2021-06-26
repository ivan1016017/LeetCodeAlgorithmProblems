from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.li = [0] * (n + 1)
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.li[idKey - 1] = value
        end = self.li.index(0)
        k = self.ptr
        self.ptr = end
        return self.li[k:end]



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)