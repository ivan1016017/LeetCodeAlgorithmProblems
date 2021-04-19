class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        value = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

        temp_1 = 0
        temp_2 = 0
        len_num1 = len(num1)
        for i in range(len(num1)):
            temp_1 += value[num1[i]]*(10**(len_num1-1-i))

        len_num2 = len(num2)
        for i in range(len(num2)):
            temp_2 += value[num2[i]]*(10**(len_num2-1-i))


        return str(temp_2 *temp_1)

solution = Solution()
print(solution.multiply("32","30"))
