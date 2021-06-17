from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        index_max = self.indexMaX(candies)
        temp: List = list()
        len_candies = len(candies)
        for i in range(len_candies):
            temp.append(candies[i] + extraCandies >= candies[index_max] )
        return temp



    def indexMaX(self, candies:List[int]) -> int:
        temp_max_index = 0
        temp_max = candies[0]
        len_candies = len(candies)
        for i in range(1,len_candies):
            if temp_max < candies[i]:
                temp_max = candies[i]
                temp_max_index = i
        return temp_max_index


solution = Solution()
# print(solution.indexMaX([]))
print(solution.kidsWithCandies([12,1,12], 10))

# print(candies[i], candies[index_max], candies[index_max],candies[i] + extraCandies >= candies[index_max])