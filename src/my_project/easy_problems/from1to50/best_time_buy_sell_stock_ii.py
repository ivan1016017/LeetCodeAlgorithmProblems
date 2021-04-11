from typing import List

if __name__ == '__main__':
    class Solution:
        def maxProfit(self, prices: List[int]) -> int:
            i = 0
            result = 0
            valley = None
            peak = None
            while i < len(prices)-1:
                print(i)

                while i < len(prices) -1 and prices[i] >= prices[i+1]:
                    i += 1

                valley = prices[i]


                while i < len(prices) -1 and prices[i] <= prices[i+1]:
                    i +=1

                peak = prices[i]

                result += peak - valley

            return result

    solution = Solution()
    print(solution.maxProfit([1,2,3,4,5]))

