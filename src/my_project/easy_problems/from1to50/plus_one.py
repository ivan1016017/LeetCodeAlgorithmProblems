from typing import List

if __name__ == '__main__':
    class Solution:
        def plusOne(self, digits: List[int]) -> List[int]:
            temp = 0
            temp_list = list()
            for i in range(len(digits)):
                temp += digits[len(digits) - 1 - i] * (10 ** i)
            temp += 1

            if temp // (10 ** len(digits)) == 0:
                for i in range(len(digits)):
                    temp_list.append(temp // (10 ** (len(digits) - 1 - i)))
                    temp -= (10 ** (len(digits) - 1 - i)) * temp_list[-1]
                return temp_list
            else:
                for i in range(len(digits) + 1):
                    temp_list.append(temp // (10 ** (len(digits) + 1 - 1 - i)))
                    temp -= (10 ** (len(digits) + 1 - 1 - i)) * temp_list[-1]
                return temp_list


    solution = Solution()
    print(solution.plusOne([8, 9, 9, 9]))
    print(124 // (10 ** (2)))
