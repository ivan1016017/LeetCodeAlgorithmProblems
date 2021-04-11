from typing import List
if __name__ == '__main__':
    class Solution:
        def removeDuplicates(self, nums: List[int]) -> int:
            print("Hello World")
            # create temp_list that store the
            temp_list = list()
            flag = False
            # check if the list contains only one element
            if len(nums) == 0:
                return 0
            elif len(nums) == 1:
                return 1
            else:
                # loop through the list
                temp_list.append(nums[0])
                length_temp_list = 1
                for i in range(len(nums)-1):
                    # initialize flag to false
                    flag = False
                    # loop through the list without the element in the first loop
                    for j in range(i+1,len(nums)):
                        # if element is repeated show flag
                        if nums[j] in temp_list:
                            flag = True
                    if flag == False:
                        temp_list.append(nums[i+1])
                        length_temp_list += 1
                for i in range(len(temp_list)):
                    nums[i] = temp_list[i]
                print(nums)
                return length_temp_list




    solution = Solution()
    print(solution.removeDuplicates([1,1,2]))



