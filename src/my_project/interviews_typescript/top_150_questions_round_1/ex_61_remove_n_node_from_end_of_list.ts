import { ListNode } from './ListNode';   

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
    // Create a dummy node to handle edge cases (e.g., removing the head)
    const dummy = new ListNode(0);
    dummy.next = head;
    
    // Initialize two pointers
    let fast: ListNode | null = dummy;
    let slow: ListNode | null = dummy;
    
    // Move fast pointer n+1 steps ahead
    for (let i = 0; i < n + 1; i++) {
        if (fast) {
            fast = fast.next;
        }
    }
    
    // Move both pointers until fast reaches the end
    while (fast !== null) {
        fast = fast.next;
        slow = slow!.next;
    }
    
    // Skip the nth node from the end
    if (slow && slow.next) {
        slow.next = slow.next.next;
    }
    
    return dummy.next;
}

