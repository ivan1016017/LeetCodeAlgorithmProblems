from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:


        len_arr = len(arr)

        for i in range(len_arr):

            if i < len_arr -1:
                arr[i] = max([num for num in arr[i+1:len(arr)]])
            if i == len_arr -1:
                arr[len_arr-1] = -1

        return arr


class SecondSolution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # We are going to start at the end of the array and move to the front
        index = len(arr) - 1
        # Our current max is -1. We initialize as -1 because it is what we want at the end of the array
        # and we will update this variable as we go through
        max_right = -1

        while index >= 0:
            # Store the value in the array in a temporary variable
            temp = arr[index]
            # Put our current max in the spot in the array
            arr[index] = max_right
            # If that temp value is grater than the current max, update it so all later values have access to it
            if temp > max_right:
                max_right = temp

            index -= 1

        return arr


solution = Solution()
print(solution.replaceElements(arr = [17,18,5,4,6,1]))