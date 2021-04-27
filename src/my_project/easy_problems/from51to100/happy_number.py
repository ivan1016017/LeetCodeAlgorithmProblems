

class Solution:
    def __init__(self):
        self.l = list()

    def isHappy(self, n: int) -> bool:
        self.l.append(n)
        if n == 1:
            return True

        else:
            x = 0
            for i in str(n):
                x = x + int(n)**2

            if x not in self.l:
                return self.isHappy(x)
            else:
                return False




