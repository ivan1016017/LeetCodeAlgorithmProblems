if __name__ == '__main__':
    class Solution:
        def convertToTitle(self, columnNumber: int) -> str:

            dict_numbers = {1: "A", 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K',
                            12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U',
                            22: 'V', 23: 'W',
                            24: 'X', 25: 'Y', 26:'Z', 0:'Z'}
            if columnNumber < 27:
                return dict_numbers[columnNumber]
            if columnNumber % 26 == 0:
                return self.convertToTitle(columnNumber//27) + dict_numbers[columnNumber%26]
            return self.convertToTitle(columnNumber//26) + dict_numbers[columnNumber%26]


    solution = Solution()
    print(solution.convertToTitle(52))
    # print(701%26)
    # print(701//26)