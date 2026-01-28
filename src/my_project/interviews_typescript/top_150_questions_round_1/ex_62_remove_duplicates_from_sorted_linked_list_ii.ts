import { ListNode } from './ListNode';   

function deleteDuplicates(head: ListNode | null): ListNode | null {
    // Create a dummy node to handle edge cases where head is removed
    const dummy = new ListNode(0);
    dummy.next = head;
    let prev = dummy;
    
    while (head) {
        // Check if current node has duplicates
        if (head.next && head.val === head.next.val) {
            // Skip all nodes with the same value
            while (head.next && head.val === head.next.val) {
                head = head.next;
            }
            // Link prev to the node after duplicates
            prev.next = head.next;
        } else {
            // No duplicate, move prev forward
            prev = prev.next!;
        }
        
        // Move to next node
        head = head.next;
    }
    
    return dummy.next;
}