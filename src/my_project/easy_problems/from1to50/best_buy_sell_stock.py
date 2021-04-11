from typing import List

if __name__ == '__main__':
    class Solution:
        def maxProfit(self, prices: List[int]) -> int:
            # initialize result
            temp = 0
            len_prices = len(prices)
            # loop through the list
            for i in range(len_prices-1):
                # loop through the remainder
                for j in range(i+1, len_prices):
                    # check if the value is greater than the current max
                    # store the value if it happens
                    if prices[j] - prices[i] >= temp:
                        temp = prices[j] - prices[i]
            return temp

    solution = Solution()
    print(solution.maxProfit([]))