from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final_answer = []

        def back(answer=[]):
            if len(answer) == len(nums):
                final_answer.append(answer)
                return
            for each_num in nums:
                if each_num not in answer:
                    new_arr = answer + [each_num]
                    back(new_arr)

        back()
        return final_answer