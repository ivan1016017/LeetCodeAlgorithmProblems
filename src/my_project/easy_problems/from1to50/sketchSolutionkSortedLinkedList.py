from typing import List


if __name__ == '__main__':
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    class Solution:

        def __init__(self):
            self.head = None

        def mergeKLists(self, lists: List[ListNode]) -> ListNode:
            list_node_to_list = self.ListNodeToList(lists)
            sorted_list = self.merge_sort(list_node_to_list,0, len(list_node_to_list)-1)
            list_to_listNode = self.from_list_listNode(sorted_list)
            if list_to_listNode == []:
                list_to_listNode = ListNode(0)
            return list_to_listNode

        def merge(self, A, p, q, r):
            # r,p and q are the indexes in the array

            # assign the values to temp arrays
            l_array = list();
            r_array = list()

            # l_array includes the q index
            for i in range(p, q + 1):
                l_array.append(A[i])
            # r_array does not include q index
            for j in range(q + 1, (r + 1)):
                r_array.append(A[j])

            # merge  the lowest items first
            i = 0;
            j = 0
            for k in range(p, r + 1):
                # add the remaining r_array to A
                if i > q - p:
                    for l in range(k, r + 1):
                        A[l] = r_array[j]
                        j += 1
                    break
                # add the remaining l_array to A
                if j > r - q - 1:
                    for l in range(k, r + 1):
                        A[l] = l_array[i]
                        i += 1
                    break
                if l_array[i] <= r_array[j]:
                    A[k] = l_array[i]
                    i += 1
                    continue

                if l_array[i] > r_array[j]:
                    A[k] = r_array[j]
                    j += 1
                    continue

            return A

        def merge_sort(self, A, p, r):
            # define the conditions for recursion
            if p < r:
                # define how to split the file
                q = (p + r) // 2
                self.merge_sort(A, p, q)
                self.merge_sort(A, q + 1, r)
                self.merge(A, p, q, r)
            return A

        def ListNodeToList(self, list_nodes: List[ListNode]) -> List:

            # define the list
            temp_list = list()
            # loop through the list of ListNodes
            for i in range(len(list_nodes)):
                # insert the first element of ListNode into list
                try:
                    temp_list.append(list_nodes[i].val)
                except:
                    continue
                # check if the next element of ListNode is available
                if list_nodes[i].next:
                    # save the next element into temp_current
                    temp_current = list_nodes[i].next
                    # while loop
                    while (temp_current):
                        # insert temp_current into temp_list
                        try:
                            temp_list.append(temp_current.val)
                        except:
                            temp_list.append(temp_current)
                        # assign nexc list_nodes[i] value to temp_current
                        try: temp_current = temp_current.next
                        except:
                            break
            return temp_list



        def from_list_listNode(self, list_numbers: List[int]) -> List[ListNode]:
            # define the scenario where the list is None
            # define the scenario where the list is empty
            if list_numbers is None or list_numbers == []:
                return []
            # the list is not empty
            # loop through the list
            temp = ListNode(list_numbers[0])
            current = temp
            for i in range(len(list_numbers)-1):
                # insert list_numbers entry to the ListNode.val
                current.next = ListNode(list_numbers[i+1])
                # set the next
                current = current.next
            return temp

    #         print("Hello")
    #         print("Hello")
    #
    #
    sample1 = ListNode(9,ListNode(8,ListNode(7)))
    sample2 = ListNode(1,ListNode(2,ListNode(3,6)))
    sample3 = ListNode(100,ListNode(200,300))
    # solution = Solution()
    # second_solution = Solution()
    # list_of_listNodes = [[]]
    #
    # print(solution.ListNodeToList([sample1, sample2]))
    # solution.ListNodeToList([ListNode(1)])
    # print(second_solution.ListNodeToList(list_of_listNodes), "None case")
    # second_solution.from_list_listNode([1])
    #
    #
    # a = second_solution.from_list_listNode([1,2,3])
    # print(a.val, a.next.val, a.next.next.val, type(a))
    #
    # if not None:
    #     print("flag")
    solution = Solution()

    A = [6, 2, 3, 1, 4, 6, 1, 1, 3, 5]

    # print(solution.merge_sort(A, 0, len(A)-1))
    print(solution.ListNodeToList([sample1,sample2, sample3]))
    temp_list = solution.ListNodeToList([sample1,sample2, sample3])
    print(solution.merge_sort(temp_list, 0, len(temp_list)-1))
    temp_sorted = solution.merge_sort(temp_list, 0, len(temp_list)-1)
    print(solution.mergeKLists([]))


