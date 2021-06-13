from typing import List

class Solution:

    def findNumberContacts(self):
        temp =None
        temp_list: List = []
        target:str = None

        while temp != 'q':
            temp = input()
            if temp != 'q':
                temp_list.append(temp)
            else:
                print("Enter the target prefix:")
                target = input()
                print("Number of times of the prefix '{}' in the list:".format(target),self.findNumberOfPrefix(temp_list, target))
                break


    def findNumberOfPrefix(self, lists: List, target: str) -> int:
        # create variable that will count the values
        temp_count: int = 0
        len_target: int = len(target)
        for item in lists:
            if item[0: len_target] == target :
                temp_count += 1



        return temp_count

solution = Solution()
solution.findNumberContacts()


# print(solution.findNumberOfPrefix(['ed','edward','eddy','edson', 'bryan', 'ryan'],'ed'))