from typing import List

if __name__ == '__main__':
    class Solution:
        flag = False
        def threeSum(self, nums: List[int]) -> List[List[int]]:
            temp = list()
            temp.append([])
            if len(nums) <3:
                return []
            else:
                for i in range(len(nums)):
                    for j in range(i+1,len(nums)):
                        for k in range(j+1,len(nums)):
                            if nums[i] + nums [j] + nums[k] == 0:
                                # flag = False
                                # print(nums[i],nums[j],nums[k], flag)
                                # for m in range(len(teresmp)):
                                #     if nums[i] in temp[m] and nums[j] in temp[m] and nums[k] in temp[m]:
                                #         flag = True
                                #
                                # print(len(temp),temp)
                                # if flag == False:
                                #     temp.append([nums[i],nums[j],nums[k]])
                                temp.append([nums[i], nums[j], nums[k]])


            return self.check_duplicates(temp[1:])

        def check_duplicates(self,list_lists):
            temp_list_sets = list()
            temp_list = list()
            for i in range(len(list_lists)):
                # print(set(list_lists[i]))
                if set(list_lists[i]) not in temp_list_sets:
                    temp_list.append(list_lists[i])
                    temp_list_sets.append(set(list_lists[i]))
            # print(temp_list_sets)
            return temp_list


    solution = Solution()
    # nums = [-1, 0, 1, 2, -1, -4]
    # num_sample = [1,0,1,0,1,0]
    # print(solution.threeSum(nums))
    print(solution.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))
    # print(solution.threeSum(num_sample))

    # list_sample = [[-4, 1, 3], [-4, 4, 0], [-2, 1, 1], [-2, 4, -2], [1, -5, 4], [0,0,0], [ -5, 4,1]]
    #
    #
    #
    # print(set([1,0,4,0])==set([1,0,4]), "sets")
    #
    # print(check_duplicates(list_sample))
    # #
    # print(len(list_sample))
    # for i in range(len(list_sample)):
    #     print(0 in list_sample[i])
