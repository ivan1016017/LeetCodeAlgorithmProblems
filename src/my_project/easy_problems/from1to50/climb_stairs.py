import math

if __name__ == '__main__':
    class Solution:
        def climbStairs(self, n: int) -> int:
            j= 0
            temp = n
            count = 0
            for i in range(n):
                temp -= 2
                if temp < 0:
                    break
                else:
                    j += 1
                    count += math.comb((n- (j*2) + j), j)
            return count +1


    solution = Solution()
    print(solution.climbStairs(5))

#this is a new comment

