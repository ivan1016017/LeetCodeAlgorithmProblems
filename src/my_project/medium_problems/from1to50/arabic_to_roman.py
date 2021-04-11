


class Solution:
    def intToRoman(self, num: int) -> str:
        # define the dictionary of the roman numbers
        roman_dict = { 1: "I", 4:"IV", 5:"V", 9:"IX", 10:"X",
                      40:"XL", 50:"L", 90:"XC", 100:"C",
                      400:"CD", 500:"D", 900:"CM", 1000:"M"}
        roman_to_arab_list = [1,4,5,9,10,40,50,90,100,400,500,900,1000,4000]

        # set flag = false
        flag = False
        temp = ""
        # while flag
        while not flag:
            for i in range(13):
                if num >= roman_to_arab_list[i] and num < roman_to_arab_list[i+1]:
                    temp += roman_dict[roman_to_arab_list[i]]
                    num -= roman_to_arab_list[i]
                    break
            if num == 0:
                flag = True


        return temp

solution = Solution()
print(solution.intToRoman(49))
