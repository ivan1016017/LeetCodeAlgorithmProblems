from typing import List



if __name__ == '__main__':
    class Solution:
        def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
            len_list = len(nums)
            temp = list()
            if len(nums) <=3:
                return []
            for i in range(len_list-3):
                for j in range(i+1,len_list-2):
                    for k in range(j+1,len_list-1):
                        for l in range(k+1,len_list):
                            if nums[i] + nums[j] + nums[k] + nums[l] == target:
                                temp.append([nums[i],nums[j],nums[k],nums[l]])
            return self.unique_list(temp)

        def unique_list(self, lists: List[List[int]]) -> List[List[int]]:
            temp_list_lists = list()
            temp_list_sets = list()

            if lists == []:
                return []
            for i in lists:
                if set(i) not in temp_list_sets:
                    temp_list_sets.append(set(i))
                    temp_list_lists.append(i)
            return temp_list_lists





    solution = Solution()
    print(solution.unique_list([[1,2,1],[2,1,1],[1,1,1]]))
    print(solution.fourSum([1,2],0)) # testing

    for i, j in  enumerate("abcd"):
        print(i,j)