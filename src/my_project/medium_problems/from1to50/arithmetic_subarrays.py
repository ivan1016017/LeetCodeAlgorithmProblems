from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        # initialize subarrays
        len_query = len(l)
        flag: bool = None
        temp_list: List[int] = list()
        temp_diff: int = None
        answer: List[bool] = list()
        for i in range(len_query):
            flag = True
            temp_list = nums[l[i]:r[i] +1]
            temp_list.sort()
            temp_diff = temp_list[1] - temp_list[0]
            print(temp_diff)
            for i in range(1, len(temp_list)):
                if (temp_list[i] - temp_list[i-1]) != temp_diff:
                    flag = False
                    break
            answer.append(flag)





        return answer


solution = Solution()

print(solution.checkArithmeticSubarrays(nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]))

