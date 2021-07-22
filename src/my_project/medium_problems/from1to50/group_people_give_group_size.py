from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        final_groups=[]
        count_dict = {}
        for ind, val in enumerate(groupSizes):
            # print(count_dict)
            if val in count_dict.keys():
                if len(count_dict[val]) < val:
                    count_dict[val].append(ind)
                else:
                    final_groups.append(count_dict[val])
                    count_dict[val] = [ind]
            else:
                count_dict[val] = [ind]

        for key in count_dict.keys():
            final_groups.append(count_dict[key])
        return final_groups

solution = Solution()
print(solution.groupThePeople(groupSizes = [3,3,3,3,3,1,3]))

