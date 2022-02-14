
class ListNode {
     val: number
     next: ListNode | null
     constructor(val?: number, next?: ListNode | null) {
         this.val = (val===undefined ? 0 : val)
         this.next = (next===undefined ? null : next)
     }
 }
 

 function rotateRight(head: ListNode | null, k: number): ListNode | null {
    if (k === 0 || !head || !head.next) return head;
  
    let slow = head;
    let fast = head;
    let len = 1;
  
    while (fast.next) {
      fast = fast.next;
      len++;
    }
  
    k %= len;
    let i = len - k;
  
    while (i) {
      i--;
      fast.next = slow;
      fast = fast.next;
      slow = slow.next || slow;
      fast.next = null;
    }
  
    return slow;
  }