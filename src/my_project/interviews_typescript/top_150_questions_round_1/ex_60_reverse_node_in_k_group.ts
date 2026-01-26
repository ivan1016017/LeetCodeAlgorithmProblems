import { ListNode } from './ListNode';   

function reverseKGroup(head: ListNode | null, k: number): ListNode | null {
    // Check if we have k nodes to reverse
    let curr = head;
    let count = 0;
    while (curr && count < k) {
        curr = curr.next;
        count++;
    }
    
    // If we have k nodes, reverse them
    if (count === k) {
        // Reverse k nodes
        let prev: ListNode | null = null;
        curr = head;
        for (let i = 0; i < k; i++) {
            const nextNode = curr!.next;
            curr!.next = prev;
            prev = curr;
            curr = nextNode;
        }
        
        // head is now the last node in reversed group
        // prev is the new head of this group
        // curr is the start of next group
        // Recursively reverse next groups
        head!.next = reverseKGroup(curr, k);
        return prev;
    }
    
    // Less than k nodes remaining, return as is
    return head;
}     