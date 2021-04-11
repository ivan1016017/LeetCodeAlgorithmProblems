from typing import List
import math

if __name__ == "__main__":
    class Solution:
        def singleNumber(self, nums: List[int]) -> int:
            # initialize flag
            flag = False
            temp_list = list()
            temp_dict = dict()

            for item in nums:
                if item not in temp_list:
                    temp_dict[item] = False
                    temp_list.append(item)
                    continue
                if item in temp_list:
                    temp_dict[item] = True
            result = [x for x in temp_dict if temp_dict[x] == False]
            return result[0]



    solution = Solution()
    print(solution.singleNumber([1]))

    sample = dict()
    sample[1] = 1*10
    sample[2] = 2*10
    print(sample[2])
    for i, j in sample.items():
        print(i,j)
        print(type(i),type(j))

    for i in sample:
        print(i)
