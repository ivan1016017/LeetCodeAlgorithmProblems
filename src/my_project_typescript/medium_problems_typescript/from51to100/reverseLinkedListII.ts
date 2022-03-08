
  class ListNode {
      val: number
      next: ListNode | null
      constructor(val?: number, next?: ListNode | null) {
          this.val = (val===undefined ? 0 : val)
          this.next = (next===undefined ? null : next)
      }
  }


function reverseBetween(head: ListNode | null, left: number, right: number): ListNode | null {
    if (!head) return null;
     if (left === right) return head;
     let current = head, previous = null, counter = 0;
     while (current != null && counter < left - 1) {
       previous = current;
       current = <ListNode>current.next;
       counter++;
     }
     counter = 0;
     const last_node_of_first_part = previous;
     const last_node_of_sub_list = current;
     while (current != null && counter < right - left + 1) {
       let temp = current.next;
       current.next = previous;
       previous = current;
       current = <ListNode>temp;
       counter++;
     }
   
     if (last_node_of_first_part) {
       last_node_of_first_part.next = previous;
     } else {
       head = previous;
     }
     last_node_of_sub_list.next = current;
     return head;
     }