class Solution:
    def twoEggDrop(self, n: int) -> int:
        i = 1
        counter = 0
        sm = 0
        while sm<n:
            sm+=i
            i+=1
            counter+=1
        return counter