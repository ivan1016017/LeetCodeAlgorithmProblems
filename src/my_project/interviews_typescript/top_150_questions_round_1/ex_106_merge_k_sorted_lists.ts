import { ListNode } from './ListNode';   


function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
    if (lists.length === 0) return null;
    
    // Divide and conquer approach
    return mergeLists(lists, 0, lists.length - 1);
}

function mergeLists(lists: Array<ListNode | null>, left: number, right: number): ListNode | null {
    if (left === right) {
        return lists[left];
    }
    
    if (left < right) {
        const mid = Math.floor((left + right) / 2);
        const l1 = mergeLists(lists, left, mid);
        const l2 = mergeLists(lists, mid + 1, right);
        return mergeTwoLists(l1, l2);
    }
    
    return null;
}

function mergeTwoLists(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    const dummy = new ListNode(0);
    let current = dummy;
    
    while (l1 !== null && l2 !== null) {
        if (l1.val < l2.val) {
            current.next = l1;
            l1 = l1.next;
        } else {
            current.next = l2;
            l2 = l2.next;
        }
        current = current.next;
    }
    
    // Attach remaining nodes
    if (l1 !== null) {
        current.next = l1;
    }
    if (l2 !== null) {
        current.next = l2;
    }
    
    return dummy.next;
}

export { mergeKLists };