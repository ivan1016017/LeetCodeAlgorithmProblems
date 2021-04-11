from typing import List



if __name__ == '__main__':
    class Solution:
        def romanToInt(self, s: str) -> int:

            # constraints 1 <= s.length <= 15
            if len(s) >= 1 and len(s)<=15:

                # create a dictionary or function that convert roman numbers into arabic numbers
                roman_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
                # create a function that reads the laws of roman numbers


                # # initialize the teemp variable that will store the operations
                temp = roman_dict[s[len(s)-1]]
                # # loop through the string of roman numbers
                for i in range(len(s)-1):
                    # convert roman numbers into arabic numbers
                    # read from right to left, follow the roman numbers rule of subtraction
                    if roman_dict[s[len(s)-2-i]] < roman_dict[s[len(s)-1-i]]:
                        temp -= roman_dict[s[len(s)-2-i]]
                    # read from right to left, follow the roman numbers rule of addition
                    else:
                        temp += roman_dict[s[len(s) - 2 - i]]
                    pass



                return temp

            else:
                return 0

    solution = Solution()
    print(solution.romanToInt("MMCCCXCIX"))
    print("Hello")