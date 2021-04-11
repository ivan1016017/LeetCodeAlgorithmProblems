



if __name__ == '__main__':
    class Solution:
        def isPalindrome(self, x: int) -> bool:

            # negative values are not palindromes
            if x < 0:
                return False

            # positive values

            if x >=0:
                # change to string
                temp_string = str(x)

                #check the palindrome condition
                temp_bool = True

                for i in range(len(temp_string)):

                    if temp_string[i] != temp_string[len(temp_string)-1-i]:
                        temp_bool = False
                        break

                return temp_bool
