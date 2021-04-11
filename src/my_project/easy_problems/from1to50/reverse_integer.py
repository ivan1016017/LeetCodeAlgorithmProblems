


if __name__ == '__main__':
    class Solution:
        def reverse(self, x: int) -> int:

            # insert the value


            # change the order of the values
            temp = ""
            x_string = str(x)

            # if the value is positive
            if x >= 0:
                for i in range(len(x_string)):
                    temp = temp + x_string[len(x_string)-1-i]
                temp = int(temp)

            # if the value is negative
            else:
                x_string = x_string[1:]
                for i in range(len(x_string)):
                    temp = temp + x_string[len(x_string)-1-i]
                temp = - int(temp)

            # check the bounds of the values


            if temp > (2**31 -1) or temp < -(2**31):
                temp = 0

            # return the value
            return temp


    solution = Solution()
    print(solution.reverse(123))
