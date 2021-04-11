

if __name__ == '__main__':
    class Solution:
        def mySqrt(self, x: int) -> int:

            if x == 0:
                return 0
            elif x == 1 or x == 2 or x == 3:
                return 1
            elif x >= 4 and x <= 8:
                return 2

            elif x > 3:
                for i in range(x//2):
                    if i ** 2 > x:
                        return i-1



    solution = Solution()
    print(solution.mySqrt(10))
    print(9//2)



