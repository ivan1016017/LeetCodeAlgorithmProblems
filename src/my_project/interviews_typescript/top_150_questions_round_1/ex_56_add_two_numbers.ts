import { ListNode } from './ListNode';

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    const dummy = new ListNode(0);
    let current = dummy;
    let carry = 0;
    
    while (l1 || l2 || carry) {
        // Get values from current nodes (0 if node is null)
        const val1 = l1 ? l1.val : 0;
        const val2 = l2 ? l2.val : 0;
        
        // Calculate sum and carry
        const total = val1 + val2 + carry;
        carry = Math.floor(total / 10);
        const digit = total % 10;
        
        // Create new node with the digit
        current.next = new ListNode(digit);
        current = current.next;
        
        // Move to next nodes if available
        l1 = l1 ? l1.next : null;
        l2 = l2 ? l2.next : null;
    }
    
    return dummy.next;
}