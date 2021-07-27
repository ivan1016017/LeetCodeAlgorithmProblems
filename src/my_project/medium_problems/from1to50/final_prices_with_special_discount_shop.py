from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        # initialize variables
        solution = list()
        len_prices = len(prices)
        flag = -1

        for i in range(len_prices):
            flag = -1
            for j in range(i+1, len_prices):
                if prices[j] <= prices[i]:
                    solution.append(prices[i]-prices[j])
                    flag = 1
                    break
            if flag == 1: continue
            else:
                solution.append((prices[i]))

        return solution

solution = Solution()
print(solution.finalPrices(prices = [1,2,3,4,5]))