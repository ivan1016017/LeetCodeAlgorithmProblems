import { ListNode } from './ListNode';

function hasCycle(head: ListNode | null): boolean {
    /**
     * Floyd's Cycle Detection Algorithm (Two Pointers - Slow and Fast)
     * 
     * Time Complexity: O(n) where n is the number of nodes
     * Space Complexity: O(1) - only using two pointers
     */
    if (!head || !head.next) {
        return false;
    }
    
    let slow: ListNode | null = head;
    let fast: ListNode | null = head;
    
    while (fast && fast.next) {
        slow = slow!.next;
        fast = fast.next.next;
        
        // If slow and fast meet, there's a cycle
        if (slow === fast) {
            return true;
        }
    }
    
    return false;
}