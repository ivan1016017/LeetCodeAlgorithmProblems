

class Solution:
    def trailingZeroes(self, n: int) -> int:

        temp = str(self.factorial(n))
        flag = False
        i = 0
        while not flag:
            if temp[-(i+1)] == "0":
                i +=1
            else:
                flag = True

        return i

    def factorial(self, n: int) -> int:

        temp = 1

        if n == 0 or n ==1:
            return temp
        else:
            for i in range(1,n+1):
                temp *= i

            return temp

solution = Solution()
print(solution.trailingZeroes())

