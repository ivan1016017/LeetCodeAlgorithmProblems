import { ListNode } from './ListNode';        

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
    // Create a dummy node to simplify edge cases
    const dummy = new ListNode(0);
    let current = dummy;
    
    // Traverse both lists and merge
    while (list1 && list2) {
        if (list1.val <= list2.val) {
            current.next = list1;
            list1 = list1.next;
        } else {
            current.next = list2;
            list2 = list2.next;
        }
        current = current.next;
    }
    
    // Attach remaining nodes from either list
    if (list1) {
        current.next = list1;
    }
    if (list2) {
        current.next = list2;
    }
    
    return dummy.next;
}