import { ListNode } from './ListNode';   

function reverseBetween(head: ListNode | null, left: number, right: number): ListNode | null {
    if (!head || left === right) {
        return head;
    }
    
    // Create a dummy node to handle edge cases where left = 1
    const dummy = new ListNode(0);
    dummy.next = head;
    
    // Step 1: Move to the node before the left position
    let prev: ListNode | null = dummy;
    for (let i = 0; i < left - 1; i++) {
        prev = prev!.next;
    }
    
    // Step 2: Reverse the sublist from left to right
    // prev points to the node before left position
    // current points to the left position
    let current: ListNode | null = prev!.next;
    
    // Reverse nodes from left to right
    for (let i = 0; i < right - left; i++) {
        // Save the next node to move
        const nextNode: ListNode | null = current!.next;
        // Point current.next to the node after nextNode
        current!.next = nextNode!.next;
        // Insert nextNode right after prev
        nextNode!.next = prev!.next;
        prev!.next = nextNode;
    }
    
    return dummy.next;
}

