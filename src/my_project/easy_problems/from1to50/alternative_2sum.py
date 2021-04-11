from typing import List

if __name__ == '__main__':
    class Solution:

        def threeSum(self, nums: List[int]) -> List[List[int]]:
            found = False
            n = len(nums)
            temp = list()
            for i in range(n - 1):

                # Find all pairs with sum
                # equals to "-arr[i]"
                s = set()
                for j in range(i + 1, n):
                    x = -(nums[i] + nums[j])
                    if x in s:
                        # print(x, nums[i], nums[j])
                        temp.append([x, nums[i], nums[j]])
                        found = True
                    else:
                        s.add(nums[j])
            if found == False:
                print("No Triplet Found")
            return self.check_duplicates(temp)

        def check_duplicates(self, list_lists):
            temp_list_sets = list()
            temp_list = list()
            for i in range(len(list_lists)):
                # print(set(list_lists[i]))
                if set(list_lists[i]) not in temp_list_sets:
                    temp_list.append(list_lists[i])
                    temp_list_sets.append(set(list_lists[i]))
            # print(temp_list_sets)
            return temp_list

            # Driven source
    solution = Solution()


    print(solution.threeSum([-1,0,1,2,-1,-4]))

    print(1 in set())
