import { ListNode } from './ListNode';  

/**
 * Sort a linked list using merge sort algorithm.
 * Time: O(n log n), Space: O(log n) for recursion stack
 */
function sortList(head: ListNode | null): ListNode | null {
    if (!head || !head.next) {
        return head;
    }
    
    // Find the middle of the list
    const mid = getMid(head);
    let left: ListNode | null = head;
    let right: ListNode | null = mid.next;
    mid.next = null;  // Split the list
    
    // Recursively sort both halves
    left = sortList(left);
    right = sortList(right);
    
    // Merge the sorted halves
    return merge(left, right);
}

/**
 * Find the middle node using slow and fast pointers.
 */
function getMid(head: ListNode): ListNode {
    let slow = head;
    let fast = head.next;
    
    while (fast && fast.next) {
        slow = slow.next!;
        fast = fast.next.next;
    }
    
    return slow;
}

/**
 * Merge two sorted linked lists.
 */
function merge(list1: ListNode | null, list2: ListNode | null): ListNode | null {
    const dummy = new ListNode(0);
    let current = dummy;
    
    while (list1 && list2) {
        if (list1.val < list2.val) {
            current.next = list1;
            list1 = list1.next;
        } else {
            current.next = list2;
            list2 = list2.next;
        }
        current = current.next;
    }
    
    // Attach remaining nodes
    if (list1) {
        current.next = list1;
    }
    if (list2) {
        current.next = list2;
    }
    
    return dummy.next;
}

