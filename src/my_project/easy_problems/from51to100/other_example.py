class Solution:
    def numOfItems(self, s, startindices, endindices):
        solution = []
        len_indexes = len(startindices)
        for i in range(len_indexes):
            start = startindices[i]
            end = endindices[i]

            found_left_vertical = False
            num_item_counted = 0
            num_items_in_this_compartment = 0

            for i in range(start - 1, end):
                if found_left_vertical == False and s[i] == '|':
                    found_left_vertical = True
                elif found_left_vertical == True and s[i] == "*":
                    num_item_counted += 1
                elif found_left_vertical == True and s[i] == "|":
                    num_items_in_this_compartment += num_item_counted
                    num_item_counted = 0

            solution.append(num_items_in_this_compartment)

        return solution

# test cases
s1 = Solution()
print(s1.numOfItems('|**|*|*', [1, 1], [5, 6])) # [2, 3]
print(s1.numOfItems('*|*|*|', [1], [6]))  # [2]
print(s1.numOfItems('******|******||***||||||||**|8|', [2, 7, 8], [9, 14, 20]))  # [0,6,3]