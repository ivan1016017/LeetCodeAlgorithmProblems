from typing import List

if __name__ == '__main__':
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next


    class Solution:
        def mergeKLists(self, lists: List[ListNode]) -> ListNode:
            pass


    def merge(A, p, q, r):
        # r,p and q are the indexes in the array

        # assign the values to temp arrays
        l_array = list()
        r_array = list()

        # l_array includes the q index
        for i in range(p, q + 1):
            l_array.append(A[i])
        # r_array does not include q index
        for j in range(q + 1, (r + 1)):
            r_array.append(A[j])

        print(l_array, r_array)
        # merge  the lowest items first
        i = 0;
        j = 0
        for k in range(p, r + 1):
            print("k:", k, "i:", i)
            # add the remaining r_array to A
            if i > q - p:
                print("flag")
                for l in range(k, r + 1):
                    A[l] = r_array[j]
                    j += 1
                    print(A[l])
                break
            # add the remaining l_array to A
            if j > r - q - 1:
                for l in range(k, r + 1):
                    A[l] = l_array[i]
                    i += 1
                break
            if l_array[i] <= r_array[j]:
                A[k] = l_array[i]
                print(A[k])
                i += 1
                continue

            if l_array[i] > r_array[j]:
                A[k] = r_array[j]
                print(A[k])
                j += 1
                continue

        return A


    def merge_sort(A, p, r):
        # define the conditions for recursion
        if p < r:
            # define how to split the file
            q = (p + r) // 2
            merge_sort(A, p, q)
            merge_sort(A, q + 1, r)
            merge(A, p, q, r)


    def ListNodeToList(list: List[ListNode]) -> List:
        print("Hello")


    ListNodeToList([ListNode(1)])

    A = [6, 2, 3, 1, 4, 6, 1, 1, 3, 5]
    merge_sort(A, 0, len(A) - 1)
    print(A)
    print(merge_sort([], 0, 0))
