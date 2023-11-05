

class ListNode {
     val: number
     next: ListNode | null
     constructor(val?: number, next?: ListNode | null) {
         this.val = (val===undefined ? 0 : val)
         this.next = (next===undefined ? null : next)
     }
 }
 

 function oddEvenList(head: ListNode | null): ListNode | null {

    let odd: ListNode = new ListNode(0)
    let even: ListNode = new ListNode(0)
    let dummy1: ListNode = odd 
    let dummy2: ListNode = even 

    while (head){
        odd.next = head 
        even.next = head.next 
        odd = odd.next 
        even = even.next 
        if (even){
            head = head.next.next
        }
        else {
            head = null
        }
        odd.next = dummy2.next
    }





    return dummy1.next

};