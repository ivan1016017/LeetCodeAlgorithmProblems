class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        res = sorted(list(range(lo, hi + 1)), key=lambda a: self.computePower(a))
        return res[k - 1]



    def computePower(self, num: int):

        count = 1

        while num /2 >1:

            if num %2 == 0:
                num = num // 2
                count += 1
            else:
                num = (num*3) + 1
                count += 1
            # print(num)
        return count

solution = Solution()

print(solution.getKth(lo = 1, hi = 1, k = 1))