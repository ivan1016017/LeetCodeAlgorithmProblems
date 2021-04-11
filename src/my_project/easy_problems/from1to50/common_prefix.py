# This code runs in jupyter, and leetcode, but not in Pycharm

from typing import List
if __name__ == '__main__':

    class Solution:
        def longestCommonPrefix(self, strs: List[str]) -> str:
            # set flag boolean, and temp_index values
            flag = False
            temp_index = 0
            temp_str = ""

            # check empty list
            if len(strs) == 0 or "" in strs:
                return temp_str
            else:
                # while (flag)
                while (not flag):
                    # loop through the list of lists
                    if len(strs) == 1:
                        return temp_str + strs[0]
                    for i in range(len(strs) - 1):
                        # check if pairs of list have the same entries in the same index
                        try:
                            strs[i][temp_index]
                            strs[i + 1][temp_index]

                        except:
                            return temp_str
                        else:
                            if strs[i][temp_index] != strs[i + 1][temp_index]:
                                print("Hi")
                                flag = True
                                break

                    if not flag:
                        temp_str += strs[0][temp_index]
                        temp_index += 1
                    else:
                        break
                return temp_str


    solution = Solution()

    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
    print(solution.longestCommonPrefix(["", "a"]), "first check")
    print(solution.longestCommonPrefix([]), "second check")
    print(solution.longestCommonPrefix(["abc", "a"]), "third check")
    print(solution.longestCommonPrefix(["a", "fourth check"]))


