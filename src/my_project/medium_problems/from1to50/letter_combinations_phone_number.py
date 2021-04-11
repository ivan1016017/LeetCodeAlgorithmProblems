from operator import add
from typing import List

if __name__ == "__main__":
    class Solution:
        def letterCombinations(self, digits: str) -> List[str]:
            num_to_letter_dict = {"2":"abc","3":"def", "4":"ghi","5":"jkl",
                                  "6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
            digits = digits[::-1]
            len_sample = len(digits)
            if len_sample == 0:
                return []
            if len_sample == 1:
                return list(num_to_letter_dict[digits[0]])

            i = 0
            temp = None
            factor_two = num_to_letter_dict[digits[0] ]
            while i <= len_sample -2:
                factor_one =  num_to_letter_dict[digits[i+1]]
                self.multiply_strings(factor_one, factor_two)
                factor_two = self.multiply_strings(factor_one, factor_two)

                i += 1

            return factor_two


        def multiply_strings(self, str1:str, str2:str) -> List[str]:
            m = len(str1)
            n = len(str2)

            temp_list1 = list()
            temp_list2 = list()
            for i in range(m):
                temp_list1 += list(str1[i]*n)
            temp_list2 = list(str2)*m
            return list(map(add,temp_list1,temp_list2))




    solution = Solution()
    print(solution.multiply_strings("123","87"))
    sample = list()
    sample += [1,2,3]
    print(sample)
    # num_to_letter_dict = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
    #                       "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    # str_sample = "23456789"
    # for i in range(len(str_sample)):
    #     print(num_to_letter_dict[str_sample[i]])

    print(solution.letterCombinations("234"))

