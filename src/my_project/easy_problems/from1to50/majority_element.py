from typing import List
from faker import Faker
import random



class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        temp_dict = dict()
        temp_set = set(nums)

        for i in range(len(nums)):

            if nums[i] not in temp_dict:
                temp_dict[nums[i]] = 0
            if nums[i] in temp_dict:
                temp_dict[nums[i]] += 1
            if temp_dict[nums[i]] >= len(nums)//2:
                return nums[i]

        print(temp_dict)


# solution = Solution()
# print(solution.majorityElement([2]))


a = random.choice([1,2,3,4])
print(a)

n = 30
m = int(n // 2)
single_value = random.randint(1,300)

i =  1
temp = None
unique_list = list()
unique_index = list()
while i <= m:
    temp = random.randint(1,300)
    print(temp)
    if temp not in unique_list:
        unique_list.append(temp)
        i += 1
print(m, 'm')
print(i, "i")
print(len(unique_list),"len")
print(unique_list)
i  = 1
while i <= n-m:
    temp = random.randint(0,n-1)
    if temp not in unique_index:
        unique_index.append(temp)
        i += 1
print(i,'i')
print(len(unique_index),"len")


list_numbers = [None]*n
for i in range(m):
    list_numbers[unique_index[i]] = single_value

l = 0
for i in range(len(list_numbers)):
    if list_numbers[i] is None:
        list_numbers[i] = unique_list[l]
        l +=1

print(list_numbers)


for i in range(10):
    print(random.randint(1,10))